from django.shortcuts import render
from django.views.generic import ListView
from accounts.mixins import AttendeeRequiredMixin
from .models import Registration

class AttendeeDashboardView(AttendeeRequiredMixin, ListView):
    model = Registration
    template_name = "attendee_dashboard.html"

    def get_queryset(self):
        return (
            Registration.objects
            .filter(attendee=self.request.user)
            .select_related("event")
        )