# Generated by Django 4.0.4 on 2022-05-04 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_verifications',
            field=models.BooleanField(default=False),
        ),
    ]
