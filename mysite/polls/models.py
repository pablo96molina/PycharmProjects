from django.db import models

import datetime
from django.db import models
from django.utils import timezone
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Fecha publicación')
    ValorMarket = models.IntegerField('Monedas')
    #Ver como hacer que se cree la columna por base de datos, lo hice usando el DBLite
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Saldo = models.IntegerField('Monedas')
    def __str__(self):
        return self.choice_text
