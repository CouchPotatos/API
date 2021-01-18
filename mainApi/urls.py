from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.QuestionListView.as_view()),
    path('answers/', views.AnswerListView.as_view()),
    path('questions/<int:idQuest>/', views.QuestionDetailView.as_view()),
    path('answers/<int:idAnsw>/', views.AnswerDetailView.as_view()),  
]