from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Language(models.Model):
    title = models.CharField(max_length=30, null=True)
    Reading = models.CharField(max_length=10)
    Writing = models.CharField(max_length=10)
    Speaking = models.CharField(max_length=10)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class ProfileModel(models.Model):
    Profile_Image = models.CharField(max_length=250, blank=False)
    First_name = models.CharField(max_length=250, blank=False)
    Father_name = models.CharField(max_length=250, blank=False)
    Middle_name = models.CharField(max_length=250, blank=False)
    Last_name = models.CharField(max_length=250, blank=False)
    Full_address = models.CharField(max_length=300, blank=False)
    Birthdate = models.DateField(blank=False)
    Bio = models.CharField(max_length=300, blank=False)
    Gender = models.CharField(max_length=15, blank=False)
    Country_Birth = models.CharField(max_length=250, blank=False)
    Country_Residence = models.CharField(max_length=250, blank=False)
    Linkedin_URL = models.URLField(blank=False)
    #Mobile number verification with regex
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Mobile_Number = models.CharField(validators=[phone_regex], max_length=17, blank=False) # validators should be a list
    language = models.ManyToManyField(Language, blank=True)

    def __str__(self):
        return self.First_name
