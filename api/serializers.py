from rest_framework import serializers
from .models import skill_trees, comments, auth_user

# because the response object cannot natively handle complex data types such as django model instances

class SkillTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = skill_trees
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comments
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth_user
        fields = '__all__'