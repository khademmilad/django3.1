from django.contrib import admin
from .models import Comment,ReplyComment


admin.site.register(Comment)
admin.site.register(ReplyComment)
