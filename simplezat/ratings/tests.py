from django.test import TestCase
from django.urls import reverse

class RatingViewTest(TestCase):

    def setUp(self):
        self.url = reverse('ratings')

    def test_rating_view_should_have_question_text(self):
        response = self.client.get(self.url)

        expected = '<h1>How do we do?</h1>'
        self.assertContains(response,expected,status_code=200)

    def test_rating_view_should_show_three_ratings(self):
           response = self.client.get(self.url)




           positive_url = reverse('comments', kwargs={'rating': 'positive'})
           expected = f'<a href="{positive_url}">' \
               '<img src="/static/images/positive.png" alt="Positive"></a>'
           self.assertContains(response,expected,status_code=200)
           neutral_url = reverse('comments', kwargs={'rating': 'neutral'})
           expected = f'<a href="{neutral_url}">' \
               '<img src="/static/images/neutral.png" alt="Neutral"></a>'
           self.assertContains(response,expected,status_code=200)
           negative_url = reverse('comments', kwargs={'rating': 'negative'})
           expected = f'<a href="{negative_url}">' \
               '<img src="/static/images/negative.png" alt="Negative"></a>'
           self.assertContains(response,expected,status_code=200)

class CommentViewTest(TestCase):
    def test_comment_view_should_render_text_and_comment_from_correctly(self):
        for each in ['positive', 'abc']:
            url = reverse(
                'comments',
                kwargs={
                    'rating':each
                    }
            )
            response = self.client.get(url)
            print (response.content)
            expected = '<h1> Any comment ? </h1>'
            self.assertContains(response, expected, status_code=200)

            expected = '<form action="." method="post">'
            self.assertContains(response, expected, status_code=200)

            expected = '<input type="hidden" name="csrfmiddlewaretoken" '
            self.assertContains(response, expected, status_code=200)

            expected = '<textarea name="comment"></textarea>' \
                f'<input type="hidden" name="rating" value="{each}">'\
                '<input type="submit"></form>'
            self.assertContains(response, expected, status_code=200)

class ThanksViewTest(TestCase):
    def test_thank_view_should_render_thank_you_text(self):
        url =  reverse('thankyou')
        response = self.client.get(url)

        expected = '<h1>Thank you!</h1>'
        self.assertContains(response, expected, status_code=200)
