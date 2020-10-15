from django.contrib import admin
from .models import Post #add this to import the Post model

# Register your models here.
admin.site.register(Post) #add this to register the Post model
