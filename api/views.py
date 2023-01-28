from django.shortcuts import render

# provides a nicer interface for returning content-negotiated Web API responses, that can be rendered to multiple formats.
from rest_framework.response import Response
#  takes a list of HTTP methods that your view should respond to.
from rest_framework.decorators import api_view

# example
# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({"message": "Got some data!", "data": request.data})
#     return Response({"message": "Hello, world!"})


@api_view(['GET'])
def getData(request):
    person = {'name':'Ryan', 'age':25} 
    return Response(person)

@api_view(['GET'])
def testGetData(request):
    person = {'name':'John', 'age':21} 
    return Response(person)

# get skill tree (skill_trees_nodes, comments, likes, dislikes, user) 
# get user

# --post--
# skill tree
# user
# comment
# like, dislike
# skill_trees_nodes

# ---put---
# skill tree
# user
# comment
# skill_trees_nodes

# ---delete---
# skill tree
# user
# comment
# like
# dislike
# skill_trees_nodes


