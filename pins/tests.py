from django.contrib.auth.models import User
from .models import Pin
from rest_framework import status
from rest_framework.test import APITestCase


class PinListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_pins(self):
        adam = User.objects.get(username='adam')
        Pin.objects.create(owner=adam, title='a title')
        response = self.client.get('/pins/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)
        # print(len(response.data))

    def test_logged_in_user_can_create_pins(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/pins/', {'title': 'a title'})

        # print("Response data:", response.data)
        # print("Response status code:", response.status_code)

        count = Pin.objects.count()
        # print("Pin count:", count)

        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_user_not_logged_in_cant_create_pin(self):
        response = self.client.post('/pins/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


