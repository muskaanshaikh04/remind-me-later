# reminders/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReminderViewSet
from reminders.views import api_root

router = DefaultRouter()
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', api_root, name='api-root'),
]
