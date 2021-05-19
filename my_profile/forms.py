from django import forms
from .models import Profile
from cloudinary.models import CloudinaryField

class ProfileForm(forms.ModelForm):
    """Form definition for Profile."""

    class Meta:
        """Meta definition for Profileform."""

        model = Profile
        fields = ('email', 'image')
