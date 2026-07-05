from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.views.generic import ListView, View, DeleteView
from accounts.mixins import AttendeeRequiredMixin
from django.urls import reverse_lazy
from .models import Registration
from events.models import Event

class AttendeeDashboardView(AttendeeRequiredMixin, ListView):
    model = Registration
    template_name = "attendee_dashboard.html"

    def get_queryset(self):
        return (
            Registration.objects
            .filter(attendee=self.request.user)
            .select_related("event")
        )


class RegistrationCreateView(AttendeeRequiredMixin, View):
    template_name = "registration_new.html"

    def get(self, request, event_pk):
        event = get_object_or_404(Event, pk=event_pk)
        already_registered = Registration.objects.filter(
            attendee=request.user, event=event
        ).exists()
        return render(request, self.template_name, {
            "event": event,
            "already_registered": already_registered,
        })

    def post(self, request, event_pk):
        event = get_object_or_404(Event, pk=event_pk)
        registration, created = Registration.objects.get_or_create(
            attendee=request.user, event=event
        )
        if created:
            messages.success(request, f'You have successfully registered for "{event.title}"!')
        else:
            messages.info(request, "You were already registered for this event.")
        return redirect("event_list")
    

class RegistrationDeleteView(AttendeeRequiredMixin, DeleteView):
    model = Registration
    template_name = "registration_delete.html"
    success_url = reverse_lazy("attendee_dashboard")

    def dispatch(self, request, *args, **kwargs):
        registration = self.get_object()
        if request.user != registration.attendee:
            messages.error(request, "You do not have permission to access this page.", extra_tags='danger')
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)