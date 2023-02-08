from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import skill_trees, comments, auth_user, likes, dislikes, skill_trees_nodes
from api.serializers import CreateCommentSerializer, CreateSkillTreeSerializer, SkillTreeSerializer, UserSerializer, CommentSerializer, LikesSerializer, DislikesSerializer, SkillTreesNodesSerializer

@api_view(['GET', 'POST'])
def skillsTreeList(request):
    if request.method == 'GET':
        skillTrees = skill_trees.objects.all()
        serializer = SkillTreeSerializer(skillTrees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CreateSkillTreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
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

@api_view(['GET', 'POST'])
def commentList(request):
    if request.method == 'GET':
        comment = comments.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CreateCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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



# TODO LIST Likes and dislikes
#   - Do we need to check for duplicates it ensure that each user can only like/dislike once?
#   - Should a user not be able to both like and dislike a skilltree?
#   -
@api_view(['GET', 'POST', 'DELETE'])
def likeDetails(request, pk):
    try:
        like = likes.objects.get(pk=pk)
    except like.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LikesSerializer(like)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def dislikeDetails(request, pk):
    try:
        dislike = dislikes.objects.get(pk=pk)
    except dislike.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DislikesSerializer(dislike)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DislikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        dislike.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST', 'PUT', 'DELETE'])
def skillTreeNodeDetails(request, pk):
    try:
        skillTreeNode = skill_trees_nodes.objects.get(pk=pk)
    except skill_trees_nodes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        skillTreeNode.parent_skill_trees_node = skill_trees_nodes.objects.get(pk=skillTreeNode.parent_skill_trees_node).get_node_info
        serializer = SkillTreesNodesSerializer(skillTreeNode)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SkillTreesNodesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = SkillTreesNodesSerializer(skillTreeNode, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        skillTreeNode.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
