# Generated by Django 4.1.5 on 2023-02-08 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_skill_trees_nodes_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill_trees_nodes',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='skill_trees_nodes',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
