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
    likes = serializers.SerializerMethodField(read_only=True)
    dislikes = serializers.SerializerMethodField(read_only=True)

    def get_likes(self, obj):
        comment_likes = obj.likes_set.all()
        return LikesSerializer(comment_likes, many=True).data

    def get_dislikes(self, obj):
        comment_dislikes = obj.dislikes_set.all()
        return DislikesSerializer(comment_dislikes, many=True).data

    class Meta:
        model = comments
        fields = ['id', 'comment', 'skill_trees_id', 'user_id', 'likes', 'dislikes']

class CreateSkillTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = skill_trees
        fields = '__all__'


class SkillTreeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comments = CommentSerializer(read_only=True, many=True)
    comments_count = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField(read_only=True)
    dislikes_count = serializers.SerializerMethodField(read_only=True)

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_likes(self, obj):
        skill_tree_likes = obj.likes_set.all()
        return LikesSerializer(skill_tree_likes, many=True).data

    def get_likes_count(self, obj):
        return obj.likes_set.count()

    def get_dislikes(self, obj):
        skill_tree_dislikes = obj.dislikes_set.all()
        return DislikesSerializer(skill_tree_dislikes, many=True).data

    def get_dislikes_count(self, obj):
        return obj.dislikes_set.count()
    

    class Meta:
        model = skill_trees
        fields = ['id', 'tags', 'name', 'description', 'number_of_nodes', 'completed', 'created_at', 'user', 'comments', 'comments_count', 'likes', 'likes_count', 'dislikes', 'dislikes_count']


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




