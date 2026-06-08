from django.apps import AppConfig  # type: ignore


class ToolsConfig(AppConfig):
    default_auto_field = 'django.db.backends.BigAutoField'
    name = 'apps.tools'
    label = 'tools'


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.backends.BigAutoField'
    name = 'apps.accounts'
    label = 'accounts'
