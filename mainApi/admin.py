from django.contrib import admin
from .models import Question, Answer


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'goto')
    list_filter = ('id', 'text')


admin.site.register(Answer, AnswerAdmin)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'message_before_question', 'image')
    list_filter = ('id', 'text')
