from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import CustomUser

class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.user = CustomUser.objects.create_user(**self.user_data)
        self.token = self.client.post('/api/login/', self.user_data, format='json').data['token']
        self.auth_header = f'Token {self.token}'

    def test_user_registration(self):
        new_user_data = {
            'email': 'newuser@example.com',
            'username': 'newuser',
            'password': 'newpassword'
        }
        response = self.client.post('/api/register/', new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)
        self.assertEqual(response.data['email'], new_user_data['email'])
        self.assertEqual(response.data['username'], new_user_data['username'])

    def test_user_login(self):
        response = self.client.post('/api/login/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_list_users_authenticated(self):
        response = self.client.get('/api/users/', HTTP_AUTHORIZATION=self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_user_authenticated(self):
        response = self.client.get(f'/api/users/{self.user.id}/', HTTP_AUTHORIZATION=self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.user.id)
        self.assertEqual(response.data['email'], self.user.email)
        self.assertEqual(response.data['username'], self.user.username)

    def test_update_user_authenticated(self):
        updated_data = {'email': 'updated@example.com', 'username': 'updateduser'}
        response = self.client.put(f'/api/users/{self.user.id}/', updated_data, HTTP_AUTHORIZATION=self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, updated_data['email'])
        self.assertEqual(self.user.username, updated_data['username'])

    def test_delete_user_authenticated(self):
        response = self.client.delete(f'/api/users/{self.user.id}/', HTTP_AUTHORIZATION=self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(CustomUser.DoesNotExist):
            CustomUser.objects.get(id=self.user.id)
