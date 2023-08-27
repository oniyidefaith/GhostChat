from django.urls import path
from . import views

app_name = 'question'
urlpatterns = [

    path('question/', views.create_questions, name='question'),
    path('list_question/', views.list_question, name='list_question'),
    path('construction/', views.construction_view, name='construction')
]
