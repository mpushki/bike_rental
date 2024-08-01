from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountAdmin(UserAdmin):
    list_display = (
        'name', 'email'
    )
    ordering = ["email"]

    fieldsets = [
        ["Personal info", {"fields": ["name"]}],
        ["Permissions", {"fields": ["is_superuser", "groups", "user_permissions"]}],
        [None, {"fields": ["email", "password"]}],
    ]
    add_fieldsets = [
        [None, {"fields": ["email", "password1", "password2"]}],
    ]


admin.site.register(Account, AccountAdmin)
