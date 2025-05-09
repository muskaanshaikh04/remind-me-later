# reminders/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Reminder
import json
from datetime import date, time

class ReminderAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_reminder = {
            'date': '2025-06-01',
            'time': '14:30:00',
            'message': 'Test reminder',
            'reminder_type': 'EMAIL',
            'recipient': 'test@example.com'
        }
        self.invalid_email_reminder = {
            'date': '2025-06-01',
            'time': '14:30:00',
            'message': 'Test reminder',
            'reminder_type': 'EMAIL',
            'recipient': 'invalid-email'
        }
        self.invalid_sms_reminder = {
            'date': '2025-06-01',
            'time': '14:30:00',
            'message': 'Test reminder',
            'reminder_type': 'SMS',
            'recipient': 'abc'  # Invalid phone number
        }
    
    def test_create_valid_reminder(self):
        """Test creating a valid reminder"""
        response = self.client.post(
            reverse('reminder-list'),
            data=json.dumps(self.valid_reminder),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reminder.objects.count(), 1)
        self.assertEqual(Reminder.objects.get().message, 'Test reminder')
    
    def test_create_invalid_email_reminder(self):
        """Test creating a reminder with invalid email"""
        response = self.client.post(
            reverse('reminder-list'),
            data=json.dumps(self.invalid_email_reminder),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_invalid_sms_reminder(self):
        """Test creating a reminder with invalid phone number"""
        response = self.client.post(
            reverse('reminder-list'),
            data=json.dumps(self.invalid_sms_reminder),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_get_reminders(self):
        """Test retrieving all reminders"""
        # Create test reminder first
        Reminder.objects.create(
            date=date(2025, 6, 1),
            time=time(14, 30),
            message='Test reminder',
            reminder_type='EMAIL',
            recipient='test@example.com'
        )
        
        response = self.client.get(reverse('reminder-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_update_reminder(self):
        """Test updating a reminder"""
        # Create test reminder first
        reminder = Reminder.objects.create(
            date=date(2025, 6, 1),
            time=time(14, 30),
            message='Original message',
            reminder_type='EMAIL',
            recipient='test@example.com'
        )
        
        updated_data = {
            'message': 'Updated message'
        }
        
        response = self.client.patch(
            reverse('reminder-detail', kwargs={'pk': reminder.id}),
            data=json.dumps(updated_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Reminder.objects.get(id=reminder.id).message, 'Updated message')
    
    def test_delete_reminder(self):
        """Test deleting a reminder"""
        reminder = Reminder.objects.create(
            date=date(2025, 6, 1),
            time=time(14, 30),
            message='Test reminder',
            reminder_type='EMAIL',
            recipient='test@example.com'
        )
        
        response = self.client.delete(reverse('reminder-detail', kwargs={'pk': reminder.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reminder.objects.count(), 0)
