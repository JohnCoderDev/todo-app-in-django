from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailTaskView.as_view(), name='task_detail'),
    path('<int:task_id>/mark_as_complete', views.mark_as_complete, name='mark_as_complete')
]
