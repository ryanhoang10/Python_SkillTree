from rest_framework import serializers
from .models import skill_trees

class SkillTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = skill_trees
        fields = [
            'id',
            'name',
            'number_of_nodes',
            'completed',
            'created_at',
            'tag_ids',
            'user_id_id'
        ]