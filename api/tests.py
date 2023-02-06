from rest_framework.test import APITestCase
from rest_framework import status
from .models import skill_trees
import json
# from django.db.backends.postgresql.features import DatabaseFeatures

# DatabaseFeatures.can_defer_constraint_checks = False

class SkillTreeApi(APITestCase):
    def test_all_get_request(self):
        data = [('/skilltrees', status.HTTP_200_OK), ('/comments', status.HTTP_200_OK), ('/users', status.HTTP_200_OK)]

        for request, expected in data:
            response = self.client.get(request)
            self.assertEqual(response.status_code, expected)

class SkillTreeTestCase(APITestCase):
    def test_create_skill_tree(self):
        data = {
            "tags": "1,2",
            "name": "unit testing",
            "description": "unit testing",
            "number_of_nodes": 10,
            "completed": True,
            "created_at": "2023-01-23T00:00:00Z",
            "user": 1
        }

        print(json.dumps(data))

        response = self.client.post('/skilltrees', json.dumps(data), content_type='application/json')

        print(response.content)
        print('hello world')
        print(skill_trees.objects.filter(name='unit testing'))
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# class CommentsTestCase(APITestCase):
#     def test_create_comment(self):
#         data = {
#             "comment": "Theo hates Larry pt2",
#             "skill_trees": 1,
#             "user": 13
#         }

#         response = self.client.post('/comments', json.dumps(data), content_type='application/json')

#         print(response)