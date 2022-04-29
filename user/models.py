from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField( max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    password = models.CharField(max_length=150, blank=False)
    mobile_phone = models.CharField( max_length=150, blank=False)
    email = models.EmailField( blank=False,unique=True)
    profile_image = models.ImageField (max_length=255, upload_to="img/%y",null=True)
    Birth_date=models.DateField(null=True)
    facebook_profile=models.URLField(max_length = 200,null=True)


    email_verified=models.BooleanField(null=True)
    @property
    def token(self):
        return '' 



#TODO in register: confirm password - image -email verification
#to do validation login 