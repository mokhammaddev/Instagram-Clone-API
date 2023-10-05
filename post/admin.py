from django.contrib import admin
from post.models import Post, Save, Like, Story, Location, Comment


admin.site.register(Save)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Story)
admin.site.register(Location)
admin.site.register(Comment)
