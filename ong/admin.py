from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.
from .models import *


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (  # new fieldset added on to the bottom
            "Custom Field Heading",  # group heading of your choice; set to None for a blank space instead of a header
            {"fields": ("whatsapp", "city", "uf"),},
        ),
    )


admin.site.register(User, CustomUserAdmin)

admin.site.register(Case)
