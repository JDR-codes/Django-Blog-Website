from django.contrib import admin
from . models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'profile', 'bio', 'phone_number']
    ordering = ['id']

admin.site.register(Profile,ProfileAdmin)