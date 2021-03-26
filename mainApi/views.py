from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.decorators import api_view

from .models import Question, Answer
from .serializers import *

from django.views.decorators.csrf import csrf_protect


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


class AnswersListView(APIView):
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


class AnswerCreateView(generics.CreateAPIView):
    '''Добавление ответа'''
    serializer_class = AnswerCreateSerializer


class QuestionCreateView(generics.CreateAPIView):
    '''Добавление вопроса'''
    serializer_class = QuestionCreateSerializer


@api_view(['DELETE', ])
def delete_question_view(request, id):

    try:
        quest = Question.objects.get(id=id)
    except Question.DoesNotExist:
        data = {}
        data["failure"] = "Bad request, not found"
        return Response(data)

    if request.method == 'DELETE':
        operation = quest.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
    return Response(data=data)


@api_view(['DELETE', ])
def delete_answer_view(request, id):

    try:
        answ = Answer.objects.get(id=id)
    except Answer.DoesNotExist:
        data = {}
        data["failure"] = "Bad request, not found"
        return Response(data)

    if request.method == 'DELETE':
        operation = answ.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
    return Response(data=data)