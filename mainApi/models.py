import jwt

from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from rest_framework import permissions
from django.db import models


class Answer(models.Model):
    '''Ответы'''
    id = models.AutoField('ID ответа', primary_key=True)
    text = models.TextField('Текст ответа')
    goto = models.PositiveIntegerField('Ссылка на следующий вопрос')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Question(models.Model):
    '''Вопросы'''
    id = models.AutoField('ID вопроса', primary_key=True)
    text = models.TextField('Текст вопроса')
    message_before_question = models.TextField('Сопутствующее сообщение перед вопросом', blank=True)
    answers = models.ManyToManyField(Answer, verbose_name='Ответы на вопрос', related_name='answers')
    image = models.ImageField('Выберите своё изображение', blank=True, upload_to='Images')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

