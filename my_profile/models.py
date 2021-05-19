from django.db import models
from tinymce.models import HTMLField
# from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    # phone_number = PhoneNumberField()
    image = CloudinaryField()
    email = models.EmailField()
    contact_me = CloudinaryField()

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"