from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question, Answer
from .serializers import QuestionListSerializer, AnswerListSerializer, QuestionDetailSerializer, AnswerDetailSerializer


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
