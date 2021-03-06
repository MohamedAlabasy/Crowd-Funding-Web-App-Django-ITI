# Generated by Django 4.0.4 on 2022-05-09 16:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, validators=[django.core.validators.RegexValidator('^[A-Za-z]+$')])),
                ('last_name', models.CharField(max_length=150, validators=[django.core.validators.RegexValidator('^[A-Za-z]+$')])),
                ('password', models.CharField(max_length=150)),
                ('mobile_phone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^01[0-2,5]{1}[0-9]{8}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_image', models.ImageField(blank=True, max_length=255, null=True, upload_to='img/%y')),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('Birth_date', models.DateField(blank=True, null=True)),
                ('facebook_profile', models.URLField(blank=True, max_length=3000, null=True)),
                ('is_verifications', models.BooleanField(default=False)),
                ('is_authenticated', models.BooleanField(null=True)),
                ('auth_provider', models.CharField(default='email', max_length=255)),
                ('last_login', models.DateTimeField(null=True)),
            ],
        ),
    ]
