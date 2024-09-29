
from rest_framework.test import APIClient
from rest_framework import status
import pytest


@pytest.mark.django_db
def contact_data():
    return {
    'contact_type': 'Company',
    'name': 'Qais',
    'email': 'ali@domain.com',
    'phone': '12345678',
    'address': 'Kabul123'
}

class TestCreateContact:
    @pytest.mark.django_db
    def test_create_contact(self):
        client = APIClient()
        response = client.post('/contact/contacts/', contact_data())
        print(response.data)
        assert response.status_code == status.HTTP_201_CREATED

 
    @pytest.mark.django_db
    def test_update_contact(self):
        client = APIClient()
        response = client.post('/contact/contacts/', contact_data())
        print(response.data)
        assert response.status_code == status.HTTP_201_CREATED

        update_data = contact_data().copy()

        contact_id = response.data['id']
        response = client.put(f'/contact/contacts/{contact_id}/', update_data)
        print(response.data)
        assert response.status_code == status.HTTP_200_OK


    

    @pytest.mark.django_db
    def test_retrieve_contact(self):
        client = APIClient()

        create_response = client.post('/contact/contacts/', contact_data())
        print(create_response.data)
        assert create_response.status_code == status.HTTP_201_CREATED

        contact_id = create_response.data['id']
        retrieve_response = client.get(f'/contact/contacts/{contact_id}/')
        print(retrieve_response.data)
        assert retrieve_response.status_code == status.HTTP_200_OK
        assert retrieve_response.data['name'] == 'Qais'

    @pytest.mark.django_db
    def test_delete_contact(self):
        client = APIClient()
        create_response = client.post('/contact/contacts/', contact_data())
        print(create_response.data)
        assert create_response.status_code == status.HTTP_201_CREATED
        contact_id = create_response.data['id']
        delete_response = client.delete(f'/contact/contacts/{contact_id}/')
        assert delete_response.status_code == status.HTTP_204_NO_CONTENT







