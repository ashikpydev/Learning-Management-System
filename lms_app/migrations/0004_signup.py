# Generated by Django 3.2.3 on 2021-05-25 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0003_auto_20210520_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('retype_password', models.CharField(max_length=250)),
            ],
        ),
    ]
