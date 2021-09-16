from django import forms
from .models import ProfileModel
from django.core.validators import RegexValidator

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)

class ProfileForm(forms.ModelForm):
    class Meta():
        model = ProfileModel
        fields = '__all__'

    # # Profile_Image = forms.ImageField(upload_to='uploaded_pics/', blank=False)
    # First_name = forms.CharField(max_length=250, required=False)
    # Father_name = forms.CharField(max_length=250, required=False)
    # Middle_name = forms.CharField(max_length=250, required=False)
    # Last_name = forms.CharField(max_length=250, required=False)
    # Full_address = forms.CharField(max_length=300, required=False)
    # Birthdate = forms.DateField(required=False)
    # Bio = forms.CharField(max_length=300, required=False)
    # Country_Birth = forms.CharField(max_length=250, required=False)
    # Country_Residence = forms.CharField(max_length=250, required=False)
    # Linkedin_URL = forms.URLField(required=False)
    # #Mobile number verification with regex
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # Mobile_Number = forms.CharField(validators=[phone_regex], max_length=17, required=False) # validators should be a list
