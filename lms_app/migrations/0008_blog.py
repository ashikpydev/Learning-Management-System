# Generated by Django 3.2.3 on 2021-06-08 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms_app', '0007_auto_20210530_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_ttle', models.CharField(max_length=250)),
                ('blog_image', models.ImageField(upload_to='blog_pics')),
                ('blog_content', models.TextField()),
                ('slug', models.SlugField(max_length=250)),
                ('publish_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]