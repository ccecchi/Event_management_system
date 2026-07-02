from django.shortcuts import render
from django.urls import reverse_lazy
from accounts.mixins import OrganizerRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Event
from .forms import EventForm


class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"


class EventCreateView(OrganizerRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = "event_new.html"
    success_url = reverse_lazy("organizer_dashboard")

    def test_func(self):
        return self.request.user.is_organizer

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f'Event "{form.instance.title}" has been succesfully registered!')
        return response

class EventDeleteView(OrganizerRequiredMixin, DeleteView):
    model = Event
    template_name = "event_delete.html"
    success_url = reverse_lazy("organizer_dashboard")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user != self.object.organizer:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class OrganizerDashboardView(OrganizerRequiredMixin, ListView):
    model = Event
    template_name = "organizer_dashboard.html"

    def test_func(self):
        return self.request.user.is_organizer()

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user).order_by("date")
