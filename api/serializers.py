from rest_framework import serializers
from .models import skill_trees, comments, auth_user, likes, dislikes, skill_trees_nodes

# because the response object cannot natively handle complex data types such as django model instances

class UserSerializer(serializers.ModelSerializer):
    # skilltree - d
    class Meta:
        model = auth_user
        fields = '__all__'


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = likes
        fields = '__all__'


class DislikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = dislikes
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    likes = LikesSerializer(read_only=True, many=True)

    class Meta:
        model = comments
        fields = ['id', 'comment', 'skill_trees_id', 'user_id', 'likes']


class SkillTreeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comments = CommentSerializer(read_only=True, many=True)
    likes = LikesSerializer(read_only=True, many=True)
    dislikes = DislikesSerializer(read_only=True, many=True)

    class Meta:
        model = skill_trees
        fields = ['id', 'tags', 'name', 'number_of_nodes',
                  'completed', 'created_at', 'user', 'comments', 'likes', 'dislikes']


class SkillTreesNodesSerializer(serializers.ModelSerializer):
    # skilltree - d
    # user - d

    # {
    #     skill tree : { skill tree info in here} // top level 
    #     
    # }

    # skill_tree_node :{
    #   parent_skill_trees_node: {
    #           2 : {
    #           name:
    #           description
    #       }
    #   }
    # }

        

    class Meta:
        model = skill_trees_nodes
        fields = '__all__'




