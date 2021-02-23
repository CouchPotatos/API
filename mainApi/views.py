from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions

from .models import Question, Answer
from .serializers import QuestionListSerializer, AnswerListSerializer, QuestionDetailSerializer, AnswerDetailSerializer

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login(request):
     csrfContext = RequestContext(request)
     return render_to_response('foo.html', csrfContext)


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class QuestionListView(APIView):
    '''Вывод списка вопросов'''
    def get(self, request):
        questions = Question.objects
        serializer = QuestionListSerializer(questions, many=True)
        return Response(serializer.data)


class QuestionDetailView(APIView):
    '''Вывод полного вопроса'''
    def get(self, request, idQuest):
        question = Question.objects.get(id=idQuest)
        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data)


class AnswerListView(APIView):
    '''Вывод списка ответов'''
    def get(self, request):
        answers = Answer.objects
        serializer = AnswerListSerializer(answers, many=True)
        return Response(serializer.data)


class AnswerDetailView(APIView):
    '''Вывод полного ответа'''
    def get(self, request, idAnsw):
        answer = Answer.objects.get(id=idAnsw)
        serializer = AnswerDetailSerializer(answer)
        return Response(serializer.data)
