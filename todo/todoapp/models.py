from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    text = models.CharField(max_length=400, help_text='Task to be done')
    concluded = models.BooleanField('task concluded', default=False)
    create_date = models.DateTimeField("date created", help_text='Date that the task was created', default=timezone.now())
    conclusion_date = models.DateTimeField("date conclusion", help_text='Optional value that the task should be concluded', null=True) 
    

    def __str__(self) -> str:
        return self.text
    
    def is_old_task(self) -> bool:
        return self.create_date.date() < timezone.now().date()
