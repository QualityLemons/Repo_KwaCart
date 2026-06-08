from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model for Well-Served.
    We use AbstractUser so we can add 'Role' or 'API_Keys' later.
    """
    pass
