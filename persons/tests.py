from django.test import TestCase
from rest_framework import authentication
from .models import MorningShift
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
# Create your tests here.

class MorningShiftTestCase(TestCase):
    def setUp(self):
        MorningShift.objects.create(start_time = '10:00', end_time = '18:00')

    def test_shift_duration(self):
        """
        Test scenario to test shift duration equals 8 hour
        """
        shift = MorningShift.objects.get(pk=1)
        self.assertEqual(shift.shift_duration, '08:00')



class UserSignUpTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()

    def test_if_request_is_successfull(self):
        """
        Test Scenario to test get request returns 200 code
        """
        response = self.client.get('http://127.0.0.1:8000/api/morning_shifts/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_user_is_unauthorized(self):
        """Test Scenario to test wrong authentification attempt"""
        username = 'wrong'
        password = 'credetials'
        response = self.client.post('http://127.0.0.1:8000/api/shift/1/enroll/Amiran', {"username":username,"password":password})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_successfully_added(self):
        signup_dict = {
            'username': "admin",
            'password1': 'admin',
        }
        response = self.client.post('http://127.0.0.1:8000/api/shift/1/enroll/Amiran', signup_dict)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)