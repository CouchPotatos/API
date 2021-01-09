from django.contrib import admin
# Register your models here.
from .models import Question, Answer


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'goto')
    list_filter = ('id', 'text')


admin.site.register(Answer, AnswerAdmin)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'message_before_question')
    list_filter = ('id', 'text')