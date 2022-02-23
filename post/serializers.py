from dataclasses import field
from urllib import request
from rest_framework import serializers
from .models import MyPost
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Register serializer

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password = validated_data['password'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        return user.username


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'





class MyPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyPost
        fields = ['id', 'post', 'user']
    
    def create(self, validated_data):
        
        print(self)
        post = MyPost.objects.create(validated_data['post'], request.user)
        return post.post + post.user.username