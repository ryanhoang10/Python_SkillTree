# Generated by Django 4.1.5 on 2023-02-08 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_skill_trees_nodes_parent_skill_trees_node'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill_trees_nodes',
            name='description',
            field=models.CharField(default='add description', max_length=250),
        ),
        migrations.AddField(
            model_name='skill_trees_nodes',
            name='title',
            field=models.CharField(default='add title', max_length=30),
        ),
    ]
