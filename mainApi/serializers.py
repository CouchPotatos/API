from rest_framework import serializers, generics
from .models import Question, Answer


class QuestionListSerializer(serializers.ModelSerializer):
    '''Список вопросов'''
    class Meta:
        model = Question
        fields = ('id', 'text', 'message_before_question', 'answers')


class QuestionDetailSerializer(serializers.ModelSerializer):
    '''Полный вопрос'''
    image = serializers.ImageField(required=False)

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

class AnswerCreateSerializer(serializers.ModelSerializer):
    '''Добавление нового ответа'''
    class Meta:
        model = Answer
        fields = ('text', 'goto')

    def create(self, validated_data):
        answer = Answer.objects.update_or_create(
            text=validated_data.get('text', None),
            goto=validated_data.get('goto')
        )
        return answer


class QuestionCreateSerializer(serializers.ModelSerializer):
    '''Добавление нового вопроса'''
    class Meta:
        model = Question
        fields = ('text', 'message_before_question', 'answers')

    def create(self, request, *args, **kwargs):
        data = request
        new_question = Question.objects.create(text=data["text"], message_before_question=data['message_before_question'])
        for answer in data["answers"]:
            new_question.answers.add(answer)
        new_question.save()
        return new_question
