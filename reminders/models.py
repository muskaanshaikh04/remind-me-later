# reminders/models.py
from django.db import models

class Reminder(models.Model):
    status = models.CharField(
        max_length=20, 
        default="PENDING",
        choices=[
            ('PENDING', 'Pending'),
            ('SENT', 'Sent'),
            ('FAILED', 'Failed')
        ]
    )

    REMINDER_TYPES = [
        ('EMAIL', 'Email'),
        ('SMS', 'SMS'),
        # Future types can be added here
    ]
    
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(max_length=10, choices=REMINDER_TYPES)
    recipient = models.CharField(max_length=255)  # Email or phone number
    created_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Reminder for {self.recipient} on {self.date} at {self.time}"
