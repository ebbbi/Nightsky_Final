from django.contrib import admin
from .models import Post, Comment , todayemotion , search, Follow, deletetoreport, commentreport
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(todayemotion)
admin.site.register(search)
admin.site.register(Follow)
admin.site.register(deletetoreport)
admin.site.register(commentreport)