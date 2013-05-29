"""
This file contains tests for the resume app. 
"""
import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from resume.models import Resume, Employer, Position, Education

def make_resume(first_name='Buffy', 
                last_name='Summers',
                address_line1='1630 Revello Drive',
                address_line2='',
                city='Sunnydale',
                state='CA',
                zip_code='',
                phone_number='(555) 555-5555',
                email='vampslayer777@aol.com',):
    """
    This is a factory method for creating and saving resumes in the database.
    All fields in the resume class are optional arguments except those that 
    are auto-filled.
    """
    resume = Resume()
    resume.first_name = first_name
    resume.last_name = last_name
    resume.address_line1 = address_line1
    resume.address_line2 = address_line2
    resume.city = city
    resume.state = state
    resume.zip_code = zip_code
    resume.phone_number = phone_number
    resume.email = email
    resume.save()
    return resume

def make_employer(resume=make_resume(),
                  name="The Watcher's Council",
                  address_line1='Somewhere in Britain',
                  address_line2='',
                  city='British City',
                  state='British State',
                  zip_code=''):
    """
    This is a factory method for creating and saving employers in the database.
    All fields in the Employer class are optional arguments. If a corresponding
    resume is not given, a default one is created and assigned using
    make_resume().
    """
    employer = Employer()
    employer.resume = resume
    employer.name = name
    employer.address_line1 = address_line1
    employer.address_line2 = address_line2
    employer.city = city
    employer.state = state
    employer.zip_code = zip_code
    employer.save()
    return employer

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

    def test_unicode(self):
        """
        __unicode__() should return the full name, obtained by calling 
        get_full_name().
        """
        resume = make_resume()
        self.assertEqual(resume.__unicode__(), resume.get_full_name())

class ResumeViewTests(TestCase):

    def test_index_view_with_no_resumes(self):
        """
        If there are no resumes, the message 'No resumes avaliable' should 
        be displayed.
        """
        response = self.client.get(reverse('resume:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No resumes avaliable')

    def test_index_view_with_one_resume(self):
        """
        If there is only one resume in the database, display it on index page.
        """
        resume = make_resume()
        response = self.client.get(reverse('resume:index'))
        self.assertEqual(response.context['resume'], resume)

    def test_index_view_with_multiple_resumes(self):
        """
        If there is more than one resume in the database, the last one created
        should be displayed.
        """
        resume_first = make_resume()
        resume_second = make_resume(first_name='Rupert', last_name='Giles')
        response = self.client.get(reverse('resume:index'))
        self.assertEqual(response.context['resume'], resume_second)

class EmployerModelTests(TestCase):

    def test_unicode(self):
        """
        The __unicode__() method for Employer should just return the name field.
        """
        employer = make_employer()
        self.assertEqual(employer.__unicode__(), employer.name)
