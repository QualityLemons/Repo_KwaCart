from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    """User creation form for the email-as-username model.

    Inherits from Django's built-in ``UserCreationForm`` but restricts the
    fields to ``email`` only — there is no username field on this model.
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    """User change form for the admin edit view.

    Mirrors ``CustomUserCreationForm``: exposes only the ``email`` field,
    matching the email-as-username model used throughout the project.
    """

    class Meta:
        model = User
        fields = ('email',)


class ProfileEmailForm(forms.ModelForm):
    """Form that lets an authenticated user update their own email address.

    Validates that the new address is not already registered to a different
    account before saving.
    """

    class Meta:
        model = User
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={
                'autocomplete': 'email',
                'placeholder': 'you@example.com',
            }),
        }

    def clean_email(self):
        email = self.cleaned_data['email'].lower().strip()
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError(
                'That email address is already registered to another account.'
            )
        return email
