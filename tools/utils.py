"""Utility helpers shared across the tools application.

Contains:
- ``save_canvas_to_file`` — persists a base64 data-URL PNG to ``media/drawings/``
  (development) or Cloudinary (production) and returns the URL/path, deduplicating
  by content hash.
- ``extract_canvas_from_payload`` — replaces the ``canvas_data`` key in a form
  payload dict with a saved file path/URL before the payload is stored in the DB.
- ``_normalize_meta`` / ``get_tool_metadata`` — ensure every tool metadata dict
  has a predictable set of keys so templates never encounter missing variables.
- ``get_all_tools_by_category`` — groups the catalog for the catalog page view.
"""
import base64
import hashlib
import os

from django.conf import settings

from .registry import TOOL_CATALOG


def save_canvas_to_file(canvas_data, tool_slug, user_id):
    """
    Accept a data-URL PNG from the drawing canvas and persist it.

    In production (CLOUDINARY_URL present) the PNG is uploaded to Cloudinary
    as an image resource and the secure_url is returned — this survives Heroku
    dyno restarts and is immediately usable in exports.

    In development the PNG is written to media/drawings/ on the local
    filesystem and a media-relative URL is returned
    (e.g. '/media/drawings/drawing-together_7_abc123.png').

    If canvas_data is already a path/URL (not a data-URL), return it unchanged.
    If canvas_data is empty, return an empty string.
    """
    if not canvas_data:
        return ''
    if not canvas_data.startswith('data:image/'):
        return canvas_data  # already a saved path or URL

    try:
        _header, encoded = canvas_data.split(',', 1)
        png_bytes = base64.b64decode(encoded)
    except Exception:
        return ''

    # SHA-256 of the raw PNG bytes produces a short, collision-resistant
    # filename — duplicate images for the same canvas content are naturally
    # deduplicated because they hash to the same filename.
    content_hash = hashlib.sha256(png_bytes).hexdigest()[:12]
    filename = f'{tool_slug}_{user_id}_{content_hash}.png'

    if os.environ.get('CLOUDINARY_URL'):
        # Production: upload directly to Cloudinary as a persistent image asset.
        # resource_type='image' (not 'raw') so Cloudinary serves it with the
        # correct Content-Type and the URL works in <img> tags and exports.
        import cloudinary.uploader
        result = cloudinary.uploader.upload(
            png_bytes,
            resource_type='image',
            public_id=f'drawings/{filename}',
            overwrite=True,
            use_filename=False,
            unique_filename=False,
        )
        return result['secure_url']

    # Development: write to local filesystem.
    drawings_dir = os.path.join(settings.MEDIA_ROOT, 'drawings')
    os.makedirs(drawings_dir, exist_ok=True)
    filepath = os.path.join(drawings_dir, filename)
    with open(filepath, 'wb') as fh:
        fh.write(png_bytes)
    return settings.MEDIA_URL + 'drawings/' + filename


def extract_canvas_from_payload(payload, tool_slug, user_id):
    """
    If payload contains a 'canvas_data' data-URL, save it to a file
    and return a copy of payload with 'canvas_data' replaced by the
    media path/URL. Returns payload unchanged if no conversion is needed.
    """
    if not payload or 'canvas_data' not in payload:
        return payload
    canvas_data = payload.get('canvas_data', '')
    if not canvas_data or not canvas_data.startswith('data:image/'):
        return payload
    # A shallow copy is made so the original cleaned_data dict passed in by
    # the view is not mutated.
    result = dict(payload)
    result['canvas_data'] = save_canvas_to_file(canvas_data, tool_slug, user_id)
    return result


def _normalize_meta(slug, meta):
    """Return a copy of meta with guaranteed keys so templates never see missing vars."""
    if meta is None:
        return None
    m = dict(meta)
    m['slug'] = slug
    # Some older templates reference 'how_to' and newer ones reference 'how'.
    # Both keys are populated from whichever is present so either works.
    m.setdefault('how', m.get('how_to', ''))
    m.setdefault('how_to', m.get('how', ''))
    m.setdefault('what', '')
    m.setdefault('why', '')
    m.setdefault('tagline', '')
    m.setdefault('show_canvas', False)
    m.setdefault('phases', None)
    return m


def get_tool_metadata(slug):
    """Fetches full metadata for a tool, including how-to and examples."""
    return _normalize_meta(slug, TOOL_CATALOG.get(slug))


def get_all_tools_by_category():
    """Groups tools for the Catalog view."""
    grouped = {}
    for slug, meta in TOOL_CATALOG.items():
        cat = meta.get('category', 'General')
        if cat not in grouped:
            grouped[cat] = []
        # Mutates the registry entry in place to add the slug key.  This is
        # intentional and idempotent — the catalog view calls this function
        # once per request and slug is always the same value for a given entry.
        meta['slug'] = slug
        grouped[cat].append(meta)
    return grouped
