# Generated by Django 4.2.2 on 2024-04-08 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.IntegerField(choices=[(0, 'Absent'), (1, 'Present')])),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.courseregistration')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.student')),
            ],
        ),
    ]