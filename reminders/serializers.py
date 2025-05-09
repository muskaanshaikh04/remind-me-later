# reminders/serializers.py
from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        model = Reminder
        fields = ['id', 'date', 'time', 'message', 'reminder_type', 'recipient', 'is_sent']
        read_only_fields = ['id', 'created_at', 'is_sent']

    def validate(self, data):
        """
        Validate reminder data based on type
        """
        reminder_type = data.get('reminder_type')
        recipient = data.get('recipient')
        
        if reminder_type == 'EMAIL':
            # Basic email validation
            if not '@' in recipient:
                raise serializers.ValidationError("Please provide a valid email address")
        elif reminder_type == 'SMS':
            # Basic phone number validation - could be enhanced
            if not recipient.isdigit() or len(recipient) < 10:
                raise serializers.ValidationError("Please provide a valid phone number")
        
        return data
    
    def to_representation(self, instance):
        """Convert to user-friendly format for responses"""
        representation = super().to_representation(instance)
        # Format to match the FastAPI implementation
        return representation
        
    def to_internal_value(self, data):
        """Handle ISO format date/time"""
        # This will ensure proper validation of ISO date/time formats
        return super().to_internal_value(data)