from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),

    path('questions/', views.QuestionListView.as_view()),
    path('answers/', views.AnswerListView.as_view()),
    path('questions/<int:idQuest>/', views.QuestionDetailView.as_view()),
    path('answers/<int:idAnsw>/', views.AnswerDetailView.as_view()),  
]