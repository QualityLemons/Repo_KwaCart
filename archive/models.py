"""Database models for the archive application.

``ToolSession``  — a collaborative session hosted by one user; stores timer
                   state, guest-access token, and references to its export files.
``ToolInstance`` — a single user's draft or archived contribution, linked
                   either to a solo submission or to a ``ToolSession``.
``WaitingListEntry`` — email addresses collected from the public waiting-list form.
``FeatureRequest``   — feature ideas submitted from the public request page.
``AuditLog``         — append-only log of security-relevant user actions.
"""
import uuid

from django.conf import settings
from django.db import models
from django.utils.timezone import now


class ToolSession(models.Model):
    """A collaborative session of a tool, hosted by one user.

    Other logged-in users join via the session's URL. Each participant's
    contribution is captured as its own ``ToolInstance`` linked back to the
    session. Closing the session locks every contribution and triggers the
    tool's processing logic so a combined view can be shown.
    """

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='hosted_sessions',
    )
    tool_slug = models.CharField(max_length=100)
    tool_version = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    timer_started_at = models.DateTimeField(
        null=True, blank=True,
        help_text='Set when the host starts the phase timer so all clients stay in sync.',
    )
    timer_paused_at = models.DateTimeField(
        null=True, blank=True,
        help_text='Set when the host pauses the timer; cleared on resume or reset.',
    )
    timer_elapsed_before_pause = models.FloatField(
        default=0,
        help_text='Cumulative elapsed seconds before the current (or last) pause.',
    )
    pause_reminder_threshold_sec = models.IntegerField(
        default=300,
        null=True,
        blank=True,
        help_text=(
            'How many seconds of pause before a long-pause reminder appears. '
            'Null disables the reminder entirely. Default is 300 (5 minutes).'
        ),
    )

    inclusive_pacing = models.BooleanField(
        default=False,
        help_text=(
            'When true, participants see an option to activate a personal '
            'extended countdown at inclusive_pacing_multiplier × the group time.'
        ),
    )
    inclusive_pacing_multiplier = models.IntegerField(
        default=3,
        choices=[(3, '3×'), (5, '5×')],
        help_text='Time multiplier offered to participants when inclusive pacing is active.',
    )

    verbal_breakout_active = models.BooleanField(
        default=False,
        help_text=(
            'When true, the host has signalled the room to start a verbal '
            'breakout. Non-composing participants are prompted to join the '
            'discussion; AAC-composing participants are reassured their '
            'digital submission window remains open.'
        ),
    )

    guest_token = models.UUIDField(
        default=uuid.uuid4,
        help_text=(
            'Token embedded in the guest QR code URL. '
            'Anyone with this token can join as an unauthenticated guest.'
        ),
    )

    pairing_code = models.CharField(
        max_length=3,
        blank=True,
        db_index=True,
        help_text=(
            'Three-digit companion-pairing code displayed alongside the QR code. '
            'Valid while the session is open; cleared on close.'
        ),
    )

    md_file = models.FileField(upload_to='archives/md/', null=True, blank=True, max_length=500)
    rtf_file = models.FileField(upload_to='archives/rtf/', null=True, blank=True, max_length=500)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.tool_slug} session ({self.status}) hosted by {self.host}'


class ToolInstance(models.Model):
    """A user-scoped record of a tool draft / submission.

    ``user`` is nullable to support guest participants who join a session via
    the QR-code guest link without creating an account.  For guest instances
    ``guest_name`` holds the name the participant entered on the join page.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tool_instances',
        null=True,
        blank=True,
        help_text='Null for unauthenticated guest participants.',
    )
    guest_name = models.CharField(
        max_length=100,
        blank=True,
        help_text='Display name entered by a guest participant (user is null).',
    )

    session = models.ForeignKey(
        ToolSession,
        on_delete=models.CASCADE,
        related_name='instances',
        null=True,
        blank=True,
        help_text='Set when this instance is part of a collaborative session.',
    )

    tool_slug = models.CharField(max_length=100)
    tool_version = models.CharField(max_length=20)

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('archived', 'Archived'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    payload_input = models.JSONField(default=dict, help_text='The raw user inputs.')
    payload_output = models.JSONField(
        default=dict, null=True, blank=True, help_text="The tool's result."
    )

    html_file = models.FileField(upload_to='archives/html/', null=True, blank=True, max_length=500)
    md_file = models.FileField(upload_to='archives/md/', null=True, blank=True, max_length=500)
    rtf_file = models.FileField(upload_to='archives/rtf/', null=True, blank=True, max_length=500)

    attachments = models.JSONField(
        default=list,
        blank=True,
        help_text=(
            'Multimedia attachments added by this participant (audio clips, '
            'symbol-board images, etc.). Each entry is a dict with keys: '
            'type ("audio" | "image"), url (Cloudinary secure_url), '
            'public_id, name.'
        ),
    )

    composing_heartbeat_at = models.DateTimeField(
        null=True, blank=True,
        help_text=(
            'Set by session_mark_composing when an AAC user signals they are '
            'composing in external software. Expires after 15 seconds of inactivity.'
        ),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    submitted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-updated_at']
        constraints = [
            models.UniqueConstraint(
                fields=['session', 'user'],
                name='unique_session_user_instance',
                condition=models.Q(session__isnull=False),
            ),
        ]

    def __str__(self):
        identity = self.user if self.user_id else (self.guest_name or 'Guest')
        return f'{identity} - {self.tool_slug} ({self.status})'

    def archive_record(self):
        """Transition this draft to 'archived' status.

        Convenience method for direct use in views or management commands.
        The session-close flow (``session_close`` view) bypasses this method
        and sets fields directly for performance, since it processes many
        instances in a single transaction.
        """
        if self.status == 'draft':
            self.status = 'archived'
            self.submitted_at = now()
            self.save()


class WaitingListEntry(models.Model):
    """Email addresses collected from the public landing page waiting list form."""

    email = models.EmailField(unique=True)
    name = models.CharField(
        max_length=200, blank=True,
        help_text='Optional — filled in voluntarily by the visitor.',
    )
    signed_up_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-signed_up_at']
        verbose_name = 'Waiting list entry'
        verbose_name_plural = 'Waiting list entries'

    def __str__(self):
        return self.email


class FeatureRequest(models.Model):
    """Feature requests submitted from the public-facing request page."""

    name = models.CharField(
        max_length=200, blank=True,
        help_text='Optional — filled in voluntarily by the visitor.',
    )
    email = models.EmailField(
        blank=True,
        help_text='Optional — so they can be notified when the feature ships.',
    )
    title = models.CharField(
        max_length=300,
        help_text='A short summary of the feature being requested.',
    )
    description = models.TextField(
        help_text='More detail: what problem does it solve, how would it work?',
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Feature request'
        verbose_name_plural = 'Feature requests'

    def __str__(self):
        return self.title


class AuditLog(models.Model):
    """Append-only security log for significant user actions.

    Rows are never updated after creation.  New entries are created
    exclusively via ``accounts.utils.log_action``; direct ``AuditLog.objects.create``
    calls are used only in ``accounts.signals`` to avoid an import of
    ``log_action`` from within the ``archive`` app itself.
    """

    # When each action is recorded:
    #   'login'        — by the user_logged_in signal in accounts/signals.py
    #   'submit'       — not currently triggered (reserved for future use)
    #   'download'     — by secure_download and secure_session_download in views_downloads.py
    #   'access_denied'— not currently triggered (reserved for future use)
    ACTION_CHOICES = [
        ('login', 'User Login'),
        ('submit', 'Tool Submission'),
        ('download', 'File Download'),
        ('access_denied', 'Unauthorized Access Attempt'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    resource_id = models.CharField(max_length=100, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(default=dict)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.action} @ {self.timestamp:%Y-%m-%d %H:%M}'
