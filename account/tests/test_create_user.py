import pytest
from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
class TestCreateUser:
    
    def test_create_user(self):
        client = APIClient()
        
        # Define the user data
        data = {
            'email': 'testuser@example.com',
            'password': 'strongpassword123',
            'username': 'testuser'
        }
        
        # Send the POST request to register the user
        response = client.post('/auth/users/', data, format='json')
        
        # Check if the response status code is 201 Created
        assert response.status_code == status.HTTP_201_CREATED
        
        # Optional: check if the email returned matches the one provided
        assert response.data['email'] == data['email']
        print(f'Response Data {response.data}')
        
        # Ensure password is not in the response
        assert 'password' not in response.data
