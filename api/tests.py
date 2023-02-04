from rest_framework.test import APITestCase, APIRequestFactory
# from .views import skillTreeDetails
# from django.urls import reverse
from rest_framework import status


class SkillTreeTestCase(APITestCase):
    def test_skill_tree_list(self):
        response = self.client.get('/skilltrees')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
