# Generated by Django 3.2 on 2022-08-12 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
