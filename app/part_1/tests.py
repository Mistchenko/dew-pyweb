from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.urls import reverse


class Part1tTests(APITestCase):
    def test_method1(self):
        url = reverse('part-1:method-1')
        response = self.client.get(url, format='json')
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_method2(self):
        url = reverse('part-1:method-2')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_method3(self):
        # Важно! `method3` - это basename из router
        url = reverse('part_1:method3-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
