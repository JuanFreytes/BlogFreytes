from django.contrib import admin
from .models import Post, Comment
from Accounts.models import UserExtension


# Register your models here.

admin.site.register(Post)
admin.site.register(UserExtension)
admin.site.register(Comment)