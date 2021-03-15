from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import AbstractUser
from.models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=["username","email","password"]
    list_display_links=["username"]