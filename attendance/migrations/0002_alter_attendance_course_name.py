# Generated by Django 4.2.2 on 2024-04-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='course_name',
            field=models.CharField(max_length=10),
        ),
    ]
