from django.db import models
from events.models import Event
from accounts.models import CustomUser

class Registration(models.Model):
    attendee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('attendee', 'event')

    def __str__(self):
        return f'{self.event.title} - {self.attendee.username}'