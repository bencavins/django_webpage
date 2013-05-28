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

def make_resume():
    resume = Resume()
    resume.first_name = 'Buffy'
    resume.last_name = 'Summers'
    return resume

class ResumeMethodTests(TestCase):

    def test_get_full_name(self):
        """
        get_full_name() should return first_name and last_name with
        a space in between.
        """
        resume = make_resume()
        self.assertEqual(resume.get_full_name(), 'Buffy Summers')

    def test_get_full_name_with_lowercase_names(self):
        """
        get_full_name() should return first_name and last_name with a space in
        between. Both first_name and last_name should start with a capital
        letter.
        """
        resume = make_resume()
        resume.first_name = 'buffy'
        resume.last_name = 'summers'
        self.assertEqual(resume.get_full_name(), 'Buffy Summers')

    def test_get_full_name_with_strange_case(self):
        """
        get_full_name() should return first_name and last_name separated by a
        space. The first letter or each name should be capitalized and the 
        rest should be lower-case.
        """
        resume = make_resume()
        resume.first_name = 'bUfFy'
        resume.last_name = 'SUMmerS'
        self.assertEqual(resume.get_full_name(), 'Buffy Summers')
