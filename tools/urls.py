"""URL configuration for the tools application."""
from django.urls import path

from . import views

app_name = 'tools'

urlpatterns = [
    path('', views.tool_catalog, name='catalog'),
    path('pathway/', views.pathway_finder, name='pathway_finder'),

    path('<slug:tool_slug>/try/', views.tool_try, name='tool_try'),

    path('<slug:tool_slug>/draft/', views.draft_editor, name='draft_new'),
    path('<slug:tool_slug>/draft/<int:instance_id>/', views.draft_editor, name='draft_edit'),
    path('<slug:tool_slug>/autosave/', views.autosave_endpoint, name='autosave'),
    path('submit/<int:instance_id>/', views.submit_tool, name='submit'),

    path('<slug:tool_slug>/session/start/', views.session_create, name='session_create'),
    path('session/<uuid:session_id>/', views.session_detail, name='session_detail'),
    path('session/<uuid:session_id>/close/', views.session_close, name='session_close'),
    path('session/<uuid:session_id>/delete/', views.session_delete, name='session_delete'),
    path('session/<uuid:session_id>/status/', views.session_status, name='session_status'),
    path('session/<uuid:session_id>/buffer-save/', views.session_buffer_save, name='session_buffer_save'),

    path('session/<uuid:session_id>/timer/start/', views.timer_start, name='timer_start'),
    path('session/<uuid:session_id>/timer/reset/', views.timer_reset, name='timer_reset'),
    path('session/<uuid:session_id>/pause-reminder/',
         views.session_set_pause_reminder,
         name='session_set_pause_reminder'),
    path('session/<uuid:session_id>/timer-enabled/',
         views.session_set_timer_enabled,
         name='session_set_timer_enabled'),

    path('session/<uuid:session_id>/guest/<uuid:guest_token>/', views.guest_join, name='guest_join'),
    path('session/<uuid:session_id>/guest/<uuid:guest_token>/respond/', views.guest_respond, name='guest_respond'),

    path('_test/timer/', views.timer_test_page, name='timer_test_page'),
]
