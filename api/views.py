from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import skill_trees, comments, auth_user
from api.serializers import SkillTreeSerializer, UserSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def skillsTreeList(request):
    if request.method == 'GET':
        skillTrees = skill_trees.objects.all()
        serializer = SkillTreeSerializer(skillTrees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SkillTreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def skillTreeDetails(request, pk):
    try:
        skillTree = skill_trees.objects.get(pk=pk)
    except skillTree.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SkillTreeSerializer(skillTree)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SkillTreeSerializer(skillTree, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        skillTree.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def usersList(request):
    if request.method == 'GET':
        users = auth_user.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def userDetails(request, pk):
    try:
        user = auth_user.objects.get(pk=pk)
    except user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def commentDetails(request, pk):
    try:
        comment = comments.objects.get(pk=pk)
    except comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# get skill tree 🐱‍👤
# (skill_trees_nodes, comments, likes, dislikes, user)
# get user - r 🐱‍👤

# --post--
# skill tree 🐱‍👤
# user - r 🐱‍👤
# comment - r 🐱‍👤
# like, dislike -d
# skill_trees_nodes -d

# ---put---
# skill tree 🐱‍👤
# user 🐱‍👤
# comment 🐱‍👤
# skill_trees_nodes

# ---delete---
# skill tree 🐱‍👤
# user 🐱‍👤
# comment 🐱‍👤
# like
# dislike
# skill_trees_nodes
