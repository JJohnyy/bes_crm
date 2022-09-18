import os
from django.conf import settings
from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

# Create your tests here.


class LandingPageTest(TestCase):

    def test_login_url(self):
        login_url  = 'login/'
        self.assertEqual(settings.LOGIN_URL, login_url)

    def test_status_code(self):
        response = self.client.get(reverse('landing-page'))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse('landing-page'))
        self.assertTemplateUsed(response, 'landing.html')


class ConfigTest(TestCase):

    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get('SECRET_KEY')

        try:  
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'bad secret key {e.messages}'
            self.fail(msg)


User = get_user_model()

class UserTestCase(TestCase):

    def setUp(self):
        user_a = User(username='admin', password='admin')
        user_a.is_superuser = True
        user_a.is_agent = True
        user_a.save()

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
