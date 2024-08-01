from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountAdmin(UserAdmin):
    list_display = (
        'name', 'email'
    )
    ordering = ["email"]

    fieldsets = [
        ["User additional data", {"fields": ["name"]}],
        [
            "Authorization",
            {"fields": ["is_superuser", "groups", "user_permissions"]},
        ],
        ["Authentication", {"fields": ["email", "password"]}],
    ]
    add_fieldsets = [
        [
            "Authorization",
            {"fields": ["is_superuser", "groups", "user_permissions"]},
        ],
        ["Authenticated", {"fields": ["email", "password1", "password2"]}],
    ]


admin.site.register(Account, AccountAdmin)
