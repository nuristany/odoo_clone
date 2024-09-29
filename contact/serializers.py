from rest_framework import serializers
from .models import Contact, ContactGroup





class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'contact_type', 'name', 'email', 'phone', 'address']  



class ContactGroupSerializer(serializers.ModelSerializer):
    contacts = serializers.SerializerMethodField()
    class Meta:
        model = ContactGroup
        fields = ['id', 'name',  'name', 'contacts']

    def get_contacts(self, obj):
        return [contact.name for contact in obj.contacts.all()]

