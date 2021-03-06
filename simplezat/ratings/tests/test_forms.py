from django import forms
from django.test import TestCase

from ..forms import RatingForm
from ..models import Rating


class RatingFormTest(TestCase):
    def setUp(self):
        self.form = RatingForm()

    def test_from_should_have_define_fields(self):
        expected_fields = [
            'sentiment',
            'comment',
        ]
        for each in expected_fields:
            self.assertTrue(each in self.form.fields)

        self.assertEqual(len(self.form.fields), 2)

    def test_from_should_have_correct_fields_and_widgets(self):
        self.assertIsInstance(
            self.form.fields['sentiment'].widget,
            forms.HiddenInput
        )
        self.assertIsInstance(
            self.form.fields['comment'].widget,
            forms.Textarea
        )

    def test_from_with_invalide_input_should_be_invalide(self):
        data = {
            'sentiment': 'positive',
            'comment': ''
        }
        form = RatingForm(data=data)
        self.assertFalse(self.form.is_valid())

        expected = {
            'comment': ['Please write some comment..']
        }
        self.assertDictEqual(form.errors, expected)

    def test_from_with_valide_input_should_be_valide(self):
        data = {
            'sentiment': 'positive',
            'comment': 'You did great!'
        }
        form = RatingForm(data=data)
        self.assertTrue(form.is_valid())

    def test_from_with_valid_input_saved_should_save_data(self):
        data = {
            'sentiment': 'positive',
            'comment': 'You did great!'
        }
        form = RatingForm(data=data)
        form.is_valid()
        form.save()

        rating = Rating.objects.last()
        self.assertEqual(rating.sentiment, 'positive')
        self.assertEqual(rating.comment, 'You did great!')
