from rest_framework import serializers
from .models import Question, Answer


class QuestionListSerializer(serializers.ModelSerializer):
    '''Список вопросов'''
    class Meta:
        model = Question
        fields = ('id', 'text', 'message_before_question', 'answers')


class QuestionDetailSerializer(serializers.ModelSerializer):
    '''Полный вопрос'''
    class Meta:
        model = Question
        fields = ('id', 'text', 'message_before_question', 'answers')


class AnswerListSerializer(serializers.ModelSerializer):
    '''Список ответов'''
    class Meta:
        model = Answer
        fields = ('id', 'text', 'goto')


class AnswerDetailSerializer(serializers.ModelSerializer):
    '''Полный ответ'''
    class Meta:
        model = Answer
        fields = ('id', 'text', 'goto')
