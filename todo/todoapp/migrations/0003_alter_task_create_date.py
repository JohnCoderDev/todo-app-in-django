# Generated by Django 4.2.5 on 2023-09-30 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_task_concluded_alter_task_conclusion_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 30, 16, 58, 23, 260823, tzinfo=datetime.timezone.utc), help_text='Date that the task was created', verbose_name='date created'),
        ),
    ]