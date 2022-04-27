from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["login"]
    list_display_links = ["login"]
    list_filter = ["login"]

# Register your models here.
