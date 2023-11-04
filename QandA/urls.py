from django.urls import path
from . import views


app_name = 'QandA'
urlpatterns = [

    path('questions/', views.QuestionView.as_view(), name='questions')
]