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
    tags = models.CharField(max_length=128)
    name = models.CharField(max_length=30)
    number_of_nodes = models.IntegerField()
    completed = models.BooleanField()
    created_at = models.DateTimeField(max_length=30)
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)

class comments(models.Model):
    class Meta:
        db_table="comments"
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    skill_trees = models.ForeignKey(skill_trees, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()

class likes(models.Model):
    class Meta:
        db_table="likes"
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    skill_trees = models.ForeignKey(skill_trees, on_delete=models.CASCADE,null=True)
    comments = models.ForeignKey(comments, on_delete=models.CASCADE, null=True)

class dislikes(models.Model):
    class Meta:
        db_table="dislikes"
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    skill_trees = models.ForeignKey(skill_trees, on_delete=models.CASCADE, null=True)
    comments = models.ForeignKey(comments, on_delete=models.CASCADE, null=True)

class progress(models.Model):
    class Meta:
        db_table="progress"
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    skill_trees = models.ForeignKey(skill_trees, on_delete=models.CASCADE)
    completed_nodes = models.IntegerField()

class skill_trees_nodes(models.Model):
    def __str__(self):
        return "skill_trees: %s  name: %s  completed_nodes: %s  parent_skill_trees_node: %s " % (self.skill_trees.name, self.user.username, str(self.completed_nodes), str(self.parent_skill_trees_node))
    class Meta:
        db_table="skill_trees_nodes"
    @property
    def get_node_info(self):
        return {
            "id": self.pk,
            "skill_trees": self.skill_trees.name,
            "user": self.user.username,
            "completed_nodes": self.completed_nodes,
            "parent_skill_trees_node": self.parent_skill_trees_node,
        }
    skill_trees = models.ForeignKey(skill_trees, on_delete=models.CASCADE)
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    completed_nodes = models.IntegerField()
    parent_skill_trees_node = models.IntegerField(null=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)

class user_skill_trees_node_completion(models.Model):
    class Meta:
        db_table="user_skill_trees_node_completion"
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    skill_trees = models.ForeignKey(skill_trees, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=128)