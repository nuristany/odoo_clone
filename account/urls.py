from django.urls import path
from django.views.generic import TemplateView
from .views import OtpVerificationView
from . import views



urlpatterns = [
    path('', TemplateView.as_view(template_name='account/home.html')),
    path('verify-otp/', OtpVerificationView.as_view(), name='verify_otp'),

    
]