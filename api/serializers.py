from typing import ClassVar
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from blog.models import Post,Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author','post','body','created',]
        

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ['author', 'title','slug','body','status','rasm', 'comments']


class PostCreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title','slug','body','status','rasm']




