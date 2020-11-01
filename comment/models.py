from django.db import models
from blog.models import Blog
from django.contrib.auth.models import User


class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="blog")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    comment = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.blog.title

    def block_comment(self):
        if self.is_active == True:
            self.is_active = False


class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,related_name="recomment")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    re_comment = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment.blog.title
