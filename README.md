# Remind-me-later API

A Django REST API for scheduling and managing reminders via SMS and Email.

## Overview

This project provides a RESTful API endpoint for a reminder application that allows users to schedule reminders with custom messages to be delivered at specific dates and times. The API currently supports two methods of delivery:

1. Email
2. SMS

The API is designed with extensibility in mind, allowing for easy addition of new reminder delivery methods in the future.

## Features

- Create, read, update, and delete reminders
- Store reminders with date, time, message, delivery method, and recipient
- Track reminder status (Pending, Sent, Failed)
- Validation of recipient information based on the delivery method
- RESTful API design following Django REST Framework best practices

## Tech Stack

- Python 3.12.4
- Django 5.1.4
- Django REST Framework
- SQLite (default database, can be configured to use PostgreSQL)

## Installation

1. Clone the repository
   ```
   git clone https://github.com/yourusername/remind-me-later.git
   cd remind-me-later
   ```

2. Create a virtual environment and activate it
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations
   ```
   python manage.py migrate
   ```

5. Run the development server
   ```
   python manage.py runserver
   ```

## API Endpoints

### Reminders

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/reminders/` | List all reminders |
| POST   | `/api/reminders/` | Create a new reminder |
| GET    | `/api/reminders/{id}/` | Retrieve a specific reminder |
| PUT    | `/api/reminders/{id}/` | Update a specific reminder |
| PATCH  | `/api/reminders/{id}/` | Partially update a specific reminder |
| DELETE | `/api/reminders/{id}/` | Delete a specific reminder |

### Request Body Example (POST/PUT)

```json
{
  "date": "2025-05-16",
  "time": "09:00:00",
  "message": "Team meeting with marketing",
  "reminder_type": "SMS",
  "recipient": "+1234567890"
}
```

For email reminders:

```json
{
  "date": "2025-05-15",
  "time": "14:30:00",
  "message": "Call with client",
  "reminder_type": "EMAIL",
  "recipient": "user@example.com"
}
```

### Response Example

```json
{
  "id": 1,
  "date": "2025-05-15",
  "time": "14:30:00",
  "message": "Call with client",
  "reminder_type": "EMAIL",
  "recipient": "user@example.com",
  "is_sent": false,
  "status": "PENDING"
}
```

## Data Model

The `Reminder` model includes the following fields:

- `date`: Date for the reminder (DateField)
- `time`: Time for the reminder (TimeField)
- `message`: The message content (TextField)
- `reminder_type`: The delivery method (CharField with choices: EMAIL, SMS)
- `recipient`: Email address or phone number (CharField)
- `created_at`: Timestamp when the reminder was created (DateTimeField)
- `is_sent`: Status flag for whether the reminder has been sent (BooleanField)
- `status`: Current status of the reminder (CharField with choices: PENDING, SENT, FAILED)

## Testing

Run the tests using:

```
python manage.py test
```

### Example API Tests

You can test the API using curl, Postman, or any API testing tool:

```bash
# Create a new SMS reminder
curl -X POST http://localhost:8000/api/reminders/ \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-05-16",
    "time": "09:00:00",
    "message": "Team meeting with marketing",
    "reminder_type": "SMS",
    "recipient": "+1234567890"
  }'

# Create a new email reminder
curl -X POST http://localhost:8000/api/reminders/ \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-05-15",
    "time": "14:30:00",
    "message": "Call with client",
    "reminder_type": "EMAIL",
    "recipient": "user@example.com"
  }'

# Get all reminders
curl http://localhost:8000/api/reminders/

# Get a specific reminder (replace 1 with the actual ID)
curl http://localhost:8000/api/reminders/1/
```

## Implementation Details

The API is built using Django REST Framework's ViewSets for a clean and maintainable architecture. The code performs validation on the recipient field based on the reminder type (checking for valid email addresses or phone numbers).

The status tracking allows for future integration with reminder delivery systems, which would update the status once delivery is attempted.


## Author

Muskaan

## License

This project is licensed under the MIT License - see the LICENSE file for details.