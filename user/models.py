from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField( max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    password = models.CharField(max_length=150, blank=False)
    mobile_phone = models.CharField( max_length=150, blank=False)
    email = models.EmailField( blank=False,unique=True)
    email_verified=models.BooleanField(null=True)
    @property
    def token(self):
        return '' 



#TODO in register: confirm password - image -email verification
#to do validation login 