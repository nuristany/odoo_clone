from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Contact, ContactGroup
from .serializers import ContactSerializer, ContactGroupSerializer

from rest_framework import filters

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'email']
    search_fields = ['name', 'email']  

class ContactGroupViewSet(viewsets.ModelViewSet):
    queryset = ContactGroup.objects.all()
    serializer_class = ContactGroupSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']  


    
    