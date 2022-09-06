from datetime import datetime, timezone
from django.test import TestCase
from polls.models import Question

class TestModelQuestion (TestCase):

    def setUp(self) -> None:
        self.question = Question.objects.create(
            question_text="¿Cuál es la capital de España?"
        )
        
    

    def test_question_data(self):
        self.assertEqual(self.question.question_text, "¿Cuál es la capital de España?")
        self.assertEqual(self.question.has_choices(), False)

    def test_defaul_date_is_today(self):
        self.assertEqual(self.question.pub_date.date(), datetime.now().date())

    def test_otra(self):
        self.question.save()

