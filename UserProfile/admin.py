from django.contrib import admin

# Register your models here.

from .models import MyProfile, Profile, Friends

admin.site.register(MyProfile)

admin.site.register(Friends)

admin.site.register(Profile)
