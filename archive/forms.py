"""Forms for the archive application.

These are kept here rather than inside the view functions so that they follow
Django's convention of defining forms in a dedicated ``forms.py`` module.
"""
from django import forms


class WaitingListForm(forms.Form):
    name = forms.CharField(
        label='Your name (optional)', max_length=200, required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Sarah'}),
    )
    email = forms.EmailField(
        label='Your email address',
        widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
    )


class FeatureRequestForm(forms.Form):
    name = forms.CharField(
        label='Your name (optional)', max_length=200, required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Sarah'}),
    )
    email = forms.EmailField(
        label='Your email (optional)',
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
        help_text="We'll only use this to let you know when the feature ships.",
    )
    title = forms.CharField(
        label='Feature title',
        max_length=300,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. Export session results as PDF',
        }),
    )
    description = forms.CharField(
        label='Tell us more',
        widget=forms.Textarea(attrs={
            'rows': 5,
            'placeholder': (
                'What problem would this solve? '
                'How do you imagine it working?'
            ),
        }),
    )
