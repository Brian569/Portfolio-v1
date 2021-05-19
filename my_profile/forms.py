from django import forms
from .models import Profile
from cloudinary.models import CloudinaryField

class ProfileForm(forms.ModelForm):
    """Form definition for Profile."""

    class Meta:
        """Meta definition for Profileform."""

        model = Profile
        fields = ('email', 'image')

class LetterForm(forms.Form):
    """LetterForm definition."""
    your_name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Email')
    text = forms.CharField()
