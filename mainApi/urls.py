from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('questions/', views.QuestionListView.as_view()),
    path('answers/', views.AnswersListView.as_view()),
    path('question/<int:idQuest>/', views.QuestionDetailView.as_view()),
    path('answer/<int:idAnsw>/', views.AnswerDetailView.as_view()),
    path('answer/create', views.AnswerCreateView.as_view()),
    path('question/create', views.QuestionCreateView.as_view()),
    path('question/<int:id>/delete', views.delete_question_view, name="DELETE Question"),
    path('answer/<int:id>/delete', views.delete_answer_view, name="DELETE Answer"),
    path('question/<int:id>/edit', views.update_question_view, name="Edit Question"),
    path('answer/<int:id>/edit', views.update_answer_view, name="Edit Answer"),
]