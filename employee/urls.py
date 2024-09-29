from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet


router = DefaultRouter()
router.register(r'employee', EmployeeViewSet, basename='employee'),
urlpatterns = [
    path('', include(router.urls))
    # path('contact/', ContactListCreateView.as_view(), name='contact')
]
   