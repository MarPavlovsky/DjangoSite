# Generated by Django 4.2 on 2023-04-28 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0002_author_title_rename_content_article_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='MyProfile',
            name='Friends',
            field=models.ManyToManyField(to='UserProfile.MyProfile'),
        ),
    ]
