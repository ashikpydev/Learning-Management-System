# Generated by Django 3.2.3 on 2021-06-08 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0008_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_ttle',
            new_name='blog_title',
        ),
    ]
