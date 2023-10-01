# Generated by Django 4.2.5 on 2023-09-30 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_task_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='concluded',
            field=models.BooleanField(null=True, verbose_name='task concluded'),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 30, 17, 9, 29, 742098, tzinfo=datetime.timezone.utc), help_text='Date that the task was created', verbose_name='date created'),
        ),
    ]
