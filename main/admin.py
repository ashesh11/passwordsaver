from django.contrib import admin

from main.models import PasswordSaver

@admin.register(PasswordSaver)
class PasswordSaverAdmin(admin.ModelAdmin):
    list_display = ['username','app_name','password']
    list_filter = ['username', 'app_name']