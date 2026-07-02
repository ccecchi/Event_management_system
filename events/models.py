from django.db import models
from django.urls import reverse
from accounts.models import CustomUser


class Event(models.Model):
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    descr = models.TextField()
    address = models.CharField(max_length=255)
    capacity = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})
