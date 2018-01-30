from datetime import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question
from datetime import timedelta
# Create your tests here.
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + timedelta(days=22)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)