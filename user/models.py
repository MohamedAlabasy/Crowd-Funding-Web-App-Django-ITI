from django.db import models

# Create your models here.
class User(models.Model):
    ##main Data
    first_name = models.CharField( max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    password = models.CharField(max_length=150, blank=False)
    mobile_phone = models.CharField( max_length=150, blank=False)
    email = models.EmailField( blank=False,unique=True)
    profile_image = models.ImageField (max_length=255, upload_to="img/%y",null=True,blank=True)
    ##additonal Data
    country = models.CharField(max_length=30,null = True,blank=True)
    Birth_date=models.DateField(null=True,blank=True)
    facebook_profile=models.URLField(max_length = 200,null=True,blank=True)
    is_verifications=models.BooleanField(null=True)
    @property
    def token(self):
        return '' 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    



#TODO in register: confirm password - image -email verification
#to do validation login 