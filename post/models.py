from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    post = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"post_id : {self.post.id} | user_id : {self.user.id} | comment_id : {self.id}"