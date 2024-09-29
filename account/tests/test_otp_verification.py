# import pytest
# from rest_framework.test import APIClient
# from rest_framework import status
# from .models import Otp

# @pytest.mark.django_db
# class TestOtpVerification:
    
#     def test_create_user_and_send_otp(self):
#         client = APIClient()

#         # Step 1: Create user, which triggers the OTP to be sent
#         user_data = {
#             'email': 'testuser@example.com',
#             'password': 'strongpassword123',
#             'username': 'testuser'
#         }
#         response = client.post('/auth/users/', user_data, format='json')
        
#         # Ensure the user was created and OTP sent successfully
#         assert response.status_code == status.HTTP_201_CREATED
#         print(response.data)  # Optional: Check the response structure


#     def test_verify_otp(self):
#         client = APIClient()

#         # Step 1: Create a user and trigger the OTP
#         user_data = {
#             'email': 'testuser@example.com',
#             'password': 'strongpassword123',
#             'username': 'testuser'
#         }
#         client.post('/auth/users/', user_data, format='json')

#         # Step 2: Verify the OTP
#         otp_code = '612520'  # Replace this with actual logic or mock the OTP retrieval

#         otp_verification_data = {
#             'email': 'testuser@example.com',
#             'otp_code': otp_code
#         }
#         response = client.post('/verify-otp/', otp_verification_data, format='json')

#         # Print the response for debugging
#         print(response.status_code, response.data)

#         # Check that the OTP verification is successful
#         assert response.status_code == status.HTTP_200_OK



import pytest
from rest_framework.test import APIClient
from rest_framework import status
from account.models import Otp  # Import the OTP model if it's stored in the database.

@pytest.mark.django_db
class TestOtpVerification:
    
    def test_create_user_and_send_otp(self):
        client = APIClient()

        # Step 1: Create user, which triggers the OTP to be sent
        user_data = {
            'email': 'testuser@example.com',
            'password': 'strongpassword123',
            'username': 'testuser'
        }
        response = client.post('/auth/users/', user_data, format='json')
        
        # Ensure the user was created and OTP sent successfully
        assert response.status_code == status.HTTP_201_CREATED
        print(response.data)  # Optional: Check the response structure

    def test_verify_otp(self):
        client = APIClient()

        # Step 1: Create a user and trigger the OTP
        user_data = {
            'email': 'testuser@example.com',
            'password': 'strongpassword123',
            'username': 'testuser'
        }
        client.post('/auth/users/', user_data, format='json')

        # Step 2: Retrieve the OTP from the database
        # Step 2: Retrieve the OTP from the database via the related User model
        otp_instance = Otp.objects.filter(user__email=user_data['email']).first()
        otp_code = otp_instance.otp_code if otp_instance else 'invalid_otp'

        otp_verification_data = {
            'email': 'testuser@example.com',
            'otp_code': otp_code
        }
        response = client.post('/verify-otp/', otp_verification_data, format='json')

        # Print the response for debugging
        print(response.status_code, response.data)

        # Check that the OTP verification is successful
        assert response.status_code == status.HTTP_200_OK
