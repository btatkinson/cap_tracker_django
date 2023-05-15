from django.urls import path
from . import views

urlpatterns = [
    path('group_history/', views.group_history, name='group_history')

]


