
from rest_framework import serializers
from .models import User, Client


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','password','is_verified']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields = ['cc']