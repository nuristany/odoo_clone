


from rest_framework import serializers
from .models import UserAccount, Otp
from .tasks import send_otp_email
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


from django.core.exceptions import ValidationError
from rest_framework import serializers




class CustomUserCreateSerializer(serializers.ModelSerializer):
    message = serializers.CharField(read_only=True)

    class Meta:
        model = UserAccount
        fields = ['id', 'email', 'password', 'message']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # Create the user
        user = UserAccount.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        # Generate OTP for the user
        otp_instance = Otp.objects.create(
            user=user,
            otp_code=None  # The model will generate a code automatically in the save method
        )
        
        # Send OTP via email
        send_otp_email.delay(user.email, otp_instance.otp_code)  # Use Celery or any async task

        # Set the success message
        user.message = 'OTP has been sent to your email.'
        user.save()  # You may not need to save the user again; it just serves to illustrate that the message is part of the instance

        return user







class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp_code = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data.get('email')
        otp_code = data.get('otp_code')

        try:
            user = User.objects.get(email=email)
            otp = Otp.objects.get(user=user)
            if not otp.is_valid() or otp.otp_code != otp_code:
                raise serializers.ValidationError('Invalid or expired OTP.')
            return data
        except (User.DoesNotExist, otp.DoesNotExist):
            raise serializers.ValidationError('Invalid email or OTP.')

    def save(self):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        user.is_verified = True
        user.is_active = True 
        user.save()
        Otp.objects.filter(user=user).delete()

        return {
            'message': 'OTP verified successfully. Your account is active now.',
        } 

            


