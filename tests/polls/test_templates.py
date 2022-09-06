from django.test import TestCase, Client
from polls.models import Question

class TestPollsTemplates(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_index_template(self):
        question = Question.objects.create(question_text="abcde")
        response = self.client.get('/polls/', {
            'latest_question_list': [question]
        })
      
        print(response.content)
        self.assertTemplateUsed(response, 'polls/index.html')
        self.assertEquals(response.status_code, 200)
        self.assertIn(b'abcde', response.content)
        self.assertIn(b'href="/polls/1/', response.content)

        self.assertInHTML('<a href="/polls/1/">abcde</a>', response.content.decode())