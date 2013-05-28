"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime

from django.utils import timezone
from django.test import TestCase

from resume.models import Resume

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class ResumeMethodTests(TestCase):

    def test_get_full_name(self):
        """
        get_full_name() should return first_name and last_name concated with
        a space in between.
        """
        resume = Resume(first_name='Ben', last_name='Cavins')
        self.assertEqual(resume.get_full_name(), 'Ben Cavins')
