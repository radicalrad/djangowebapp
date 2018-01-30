from django.db import models
from datetime import timedelta
# Create your models here.
from datetime import datetime
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text+" published on: "+ '{:%Y-%m-%d %H:%M}'.format(self.pub_date)

    def was_published_recently(self):
        if (self.pub_date >= timezone.now() - timedelta(days=1) and self.pub_date<=timezone.now()):

            return True
        else:
            return False

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text