from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import patch
from django.test import TestCase, Client
import pytest
from auths.models import Details
from auths.views import register


class RegisterViewTestCase(TestCase):
    def setUp(self):
        super().setUp()  # Call the parent class's setUp method
        self.client = Client()

        self.patcher_send_mail = patch('django.core.mail.send_mail')
        self.mock_send_mail = self.patcher_send_mail.start()
        self.mock_send_mail.return_value = 1  # Assume email sending is successful
        self.test_user = User.objects.create_user(username='testuser', email='test@example.com',
                                                  password='testpassword')

# Rest of your test cases and test functions go here...
    def test_logout_redirect(self):
        self.client.force_login(User.objects.get_or_create(username='valid_user')[0])
        response = self.client.get('/logout/', follow=True)
        self.assertRedirects(response, '/login/')
        self.assertContains(response, 'You have been logged out')