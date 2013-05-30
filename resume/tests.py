"""
This file contains tests for the resume app. 
"""
import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from resume.models import Resume, Employer, Position, Education


def make_resume(**kwargs):
    """
    Factory method for creating and saving resumes in the test database. All
    fields in the resume class are optional arguments except those that are
    auto-filled.
    """
    default_args = {
        'first_name': 'Buffy',
        'last_name': 'Summers',
        'address_line1': '1630 Revello Drive',
        'address_line2': '',
        'city': 'Sunnydale',
        'state': 'CA',
        'zip_code': '',
        'phone_number': '(555) 555-5555',
        'email': 'vampslayer777@aol.com',
    }
    for arg in kwargs:
        default_args[arg] = kwargs[arg]
    return Resume.objects.create(**default_args)

def make_employer(**kwargs):
    """
    A factory method for creating and saving Employer objects in the database.
    All fields in the Employer class are optional arguments. If a corresponding
    resume is not given, a default one is created and assigned using 
    make_resume().
    """
    default_args = {
        'resume': make_resume(),
        'name': "The Watchers' Council",
        'address_line1': 'Somewhere in Britain',
        'address_line2': '',
        'city': 'British City',
        'state': 'British State',
        'zip_code': '',
    }
    for arg in kwargs:
        default_args[arg] = kwargs[arg]
    return Employer.objects.create(**default_args)

def make_position(**position_args):
    """
    A factory method for creating and saving Position objects in the database.
    All fields in the Position class are optional arguments. If a corresponding
    employer is not given, a default one is created and assigned using
    make_employer()
    """
    default_args = {
        'employer': make_employer(),
        'title': 'Vampire Slayer',
        'start_date': '1996-08-01',
        'end_date': None,
    }
    for arg in position_args:
        default_args[arg] = position_args[arg]
    return Position.objects.create(**default_args)

def make_education(**education_args):
    """
    A factory method for creating and saving Education objects in the database.
    All fields in the Education class are optional arguments. If a corresponding
    resume is not given, a default one is created and assigned using 
    make_resume().
    """
    default_args = {
        'resume': make_resume(),
        'name': 'Sunnydale High',
        'degree': 'High School Diploma',
        'city': 'Sunnydale',
        'state': 'CA',
        'start_date': '1997-03-10',
        'end_date': '1999-05-28',
    }
    for arg in education_args:
        default_args[arg] = education_args[arg]
    return Education.objects.create(**default_args)


class ResumeModelTests(TestCase):

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


class PositionModelTests(TestCase):

    def test_unicode(self):
        """
        The __unicode__() method for Position should return the title field.
        """
        position = make_position()
        self.assertEqual(position.__unicode__(), position.title)


class EducationModelTests(TestCase):

    def test_unicode(self):
        """
        The __unicode__() method for Education should return the name field.
        """
        education = make_education()
        self.assertEqual(education.__unicode__(), education.name)


