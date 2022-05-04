from django.db import models
from crowd_funding.settings import SECRET_KEY
import jwt
from datetime import datetime, timedelta
from django.conf import settings
# Create your models here.


class User(models.Model):
    # main Data
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    password = models.CharField(max_length=150, blank=False)
    mobile_phone = models.CharField( max_length=150, blank=False)
    email = models.EmailField( blank=False,unique=True)
    profile_image = models.ImageField (max_length=255, upload_to="img/%y",null=True,blank=True)
    ##additonal Data
    country = models.CharField(max_length=30,null = True,blank=True)
    Birth_date=models.DateField(null=True,blank=True)
    facebook_profile=models.URLField(max_length = 200,null=True,blank=True)
    is_verifications=models.BooleanField(default=False)
    is_authenticated = models.BooleanField(null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def token(self):
        token = jwt.encode({'email':self.email,
        'exp':datetime.utcnow()+timedelta(hours=24)},
        settings.SECRET_KEY,algorithm='HS256')
        return token
