from django.http import Http404
from django.shortcuts import render

from tools.utils import get_tool_metadata

from .case_studies import get_case_study, list_case_studies


def case_study_index(request):
    studies = list_case_studies()
    return render(request, 'case_studies/index.html', {'case_studies': studies})


def case_study_detail(request, slug):
    study = get_case_study(slug)
    if not study:
        raise Http404
    tool_meta = get_tool_metadata(study['tool_slug']) or {}
    return render(request, 'case_studies/detail.html', {
        'study': study,
        'tool_meta': tool_meta,
    })
