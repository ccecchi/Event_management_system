from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = {"A": "Attendee", "O": "Organizer"}
    ruolo = models.CharField(max_length=1, choices=ROLES, default="A")
