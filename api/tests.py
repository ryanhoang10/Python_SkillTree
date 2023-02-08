from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from .models import skill_trees, auth_user
import json

# class SkillTreeApi(APITestCase):
#     def test_all_get_request(self):
#         data = [
#             ('/skilltrees', status.HTTP_200_OK), 
#             ('/comments', status.HTTP_200_OK), 
#             ('/users', status.HTTP_200_OK)
#         ]

#         for request, expected in data:
#             response = self.client.get(request)
#             self.assertEqual(response.status_code, expected)

class SkillTreeTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = auth_user(
            id=1,
            password='password', 
            last_login='2023-06-02',
            is_superuser=False,
            username='Test',
            first_name='Unit',
            last_name='Testing',
            email='unit@testing.com',
            is_staff=False,
            is_active=True,
            date_joined='2023-06-02'
        )

        self.skill_tree = skill_trees(
            id=1,
            tags='1,2', 
            name='unit testing',
            description='unit testing',
            number_of_nodes=11,
            completed=True,
            created_at='2023-01-23T00:00:00Z',
        )

    def test_create_skill_tree(self):
        data = {
            "tags": "1,2",
            "name": "unit testing",
            "description": "unit testing",
            "number_of_nodes": 10,
            "completed": True,
            "created_at": "2023-01-23T00:00:00Z",
            "user": self.user.pk
        }

        print(self.user.pk)
        response = self.client.post('/skilltrees', json.dumps(data), content_type='application/json')
        print(response.content)
        # print('hereee')

    # def test_update_skill_tree(self):
        # response = self.client.put('/skilltrees/1/', json.dumps({'name': 'unit testing put'}), content_type='application/json')

        # print(response.content)
#         print(skill_trees.objects.filter(name='unit testing'))
#         # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# class CommentsTestCase(APITestCase):
#     def test_create_comment(self):
#         data = {
#             "comment": "Theo hates Larry pt2",
#             "skill_trees": 1,
#             "user": 13
#         }

#         response = self.client.post('/comments', json.dumps(data), content_type='application/json')

#         print(response)