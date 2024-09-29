from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, ContactGroupViewSet


router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact'),
router.register(r'contact-group', ContactGroupViewSet, basename='contact-group')
urlpatterns = [
    path('', include(router.urls))
    # path('contact/', ContactListCreateView.as_view(), name='contact')
]
   