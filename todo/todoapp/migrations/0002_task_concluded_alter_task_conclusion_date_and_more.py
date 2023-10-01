# Generated by Django 4.2.5 on 2023-09-30 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='concluded',
            field=models.BooleanField(default=False, verbose_name='task concluded'),
        ),
        migrations.AlterField(
            model_name='task',
            name='conclusion_date',
            field=models.DateTimeField(default=None, help_text='Optional value that the task should be concluded', verbose_name='date conclusion'),
        ),
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.CharField(help_text='Task to be done', max_length=400),
        ),
    ]
