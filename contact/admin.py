from django.contrib import admin
from .models import Contact, ContactGroup

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'contact_type', 'phone',)
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('contact_type',)

@admin.register(ContactGroup)
class ContactGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)