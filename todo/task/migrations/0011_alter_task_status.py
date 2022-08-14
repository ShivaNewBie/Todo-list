# Generated by Django 3.2 on 2022-08-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Finished', 'Finished'), ('Unfishined', 'Unfinished')], default='Unfishined', max_length=20),
        ),
    ]