# Generated by Django 4.2 on 2023-05-13 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0006_rename_name_title_title_remove_friends_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Title',
            new_name='BIO',
        ),
        migrations.RenameField(
            model_name='MyProfile',
            old_name='Content',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='bio',
            old_name='Title',
            new_name='bio',
        ),
    ]