
   
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount

class UserAccountAdmin(UserAdmin):
    # Fields to be used in displaying the User model in the admin interface
    list_display = ('email', 'is_staff', 'is_active', 'is_verified')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Verification', {'fields': ('is_verified',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'is_verified'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(UserAccount, UserAccountAdmin)