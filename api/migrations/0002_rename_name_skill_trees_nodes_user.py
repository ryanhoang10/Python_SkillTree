# Generated by Django 4.1.5 on 2023-02-08 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill_trees_nodes',
            old_name='name',
            new_name='user',
        ),
    ]
