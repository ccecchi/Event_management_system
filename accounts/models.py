from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = {"A": "Attendee", "O": "Organizer"}
    role = models.CharField(max_length=1, choices=ROLES, default="A")
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    
    def is_organizer(self) -> bool:
        return self.role == "O"