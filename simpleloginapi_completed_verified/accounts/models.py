from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    #mobile=models.IntegerField(max_length=300)
    #OTP=models.IntegerField(max_length=300)

class Register(models.Model):
    username = models.CharField(max_length=200,default=1)
    email = models.EmailField(max_length=300,default=1)
    password = models.TextField(max_length=255,default=1)
class phoneModel(models.Model):
        Mobile = models.IntegerField(blank=False, null=True,default=1)
        isVerified = models.BooleanField(blank=False, default=False)
        counter = models.IntegerField(default=0, blank=False)  # For HOTP Verification

        def __str__(self):
            return str(self.Mobile)

# This class returns the string needed to generate the key
