# Generated by Django 4.0.4 on 2022-04-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='selected_at_by_admin',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
