from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name', 'email')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],password = validated_data['password'], email = validated_data['email'])
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.save()
        return user



# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=False, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'post', 'user']
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        post = Post(**validated_data, user=user)
        post.save()
        return post

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=False, read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'user', 'post']
        read_only_fields = ('user', 'post')
    
    def create(self, validated_data):
        comment = Comment.objects.create(comment=validated_data['comment'], user=self.context['request'].user, post=validated_data['post'])
        return comment

