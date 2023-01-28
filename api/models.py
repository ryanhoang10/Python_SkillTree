from django.db import models

# Create your models here.
class tags(models.Model):
    class Meta:
        db_table="tags"
    name = models.CharField(max_length=30)

class auth_user(models.Model):
    class Meta:
        db_table="users"
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    
class skill_trees(models.Model):
    class Meta:
        db_table="skill_trees"
    tag_ids = models.CharField(max_length=128)
    name = models.CharField(max_length=30)
    number_of_nodes = models.IntegerField()
    completed = models.BooleanField()
    created_at = models.DateTimeField(max_length=30)
    user_id = models.ForeignKey(auth_user, on_delete=models.CASCADE)

class comments(models.Model):
    class Meta:
        db_table="comments"
    user_id = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    skill_trees_id = models.ForeignKey(skill_trees, on_delete=models.CASCADE)
    
class likes(models.Model):
    class Meta:
        db_table="likes"
    user_id = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    skill_trees_id = models.ForeignKey(skill_trees, on_delete=models.CASCADE)
    comments_id = models.ForeignKey(comments, on_delete=models.CASCADE)

class dislikes(models.Model):
    class Meta:
        db_table="dislikes"
    user_id = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    skill_trees_id = models.ForeignKey(skill_trees, on_delete=models.CASCADE)
    comments_id = models.ForeignKey(comments, on_delete=models.CASCADE)

class progress(models.Model):
    class Meta:
        db_table="progress"
    user_id = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    skill_trees_id = models.ForeignKey(skill_trees, on_delete=models.CASCADE)
    completed_nodes = models.IntegerField()

class skill_trees_nodes(models.Model):
    class Meta:
        db_table="skill_trees_nodes"
    skill_trees_id = models.ForeignKey(skill_trees, on_delete=models.CASCADE)
    name = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    completed_nodes = models.IntegerField()
    parent_skill_trees_node_id = models.IntegerField()

class user_skill_trees_node_completion(models.Model):
    class Meta:
        db_table="user_skill_trees_node_completion"
    user_id = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    skill_trees_id = models.ForeignKey(skill_trees, on_delete=models.CASCADE)