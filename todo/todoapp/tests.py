import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Task

# Create your tests here.
class TaskModelTests(TestCase):
    def test_is_old_task_with_question_in_the_past(self):
        """
        is_old_task() should return True when the date of
        creation of the task is smaller than today's date
        """
        past_date = timezone.now() - datetime.timedelta(days=30)
        old_task = Task(text='some task', create_date = past_date)
        self.assertIs(old_task.is_old_task(), True)

    def test_is_old_task_with_question_in_the_present(self):
        """
        is_old_task() should return False when the date of
        creation of the task is equal than today's date
        """
        today_date = timezone.now()
        today_task = Task(text='some task', create_date = today_date)
        self.assertIs(today_task.is_old_task(), False)
    
    def test_is_old_task_with_question_in_the_future(self):
        """
        is_old_task() should return False when the date of
        creation of the task is greater than today's date
        """
        future_date = timezone.now()
        future_task = Task(text='some task', create_date = future_date)
        self.assertIs(future_task.is_old_task(), False)