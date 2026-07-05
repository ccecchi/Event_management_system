from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import OrganizerRequiredMixin, AttendeeRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from .models import Event
from .forms import EventForm
from registrations.models import Registration


class EventDetailView(DetailView, LoginRequiredMixin):
    model = Event
    template_name = "event_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_organizer():
            context["is_registered"] = Registration.objects.filter(
                attendee=self.request.user, event=self.object
            ).exists()
        return context


class EventCreateView(OrganizerRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = "event_new.html"
    success_url = reverse_lazy("organizer_dashboard")

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f'Event "{form.instance.title}" has been succesfully registered!')
        return response


class EventUpdateView(OrganizerRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = "event_edit.html"


class EventDeleteView(OrganizerRequiredMixin, DeleteView):
    model = Event
    template_name = "event_delete.html"
    success_url = reverse_lazy("organizer_dashboard")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user != self.object.organizer:
            messages.error(request, "You do not have permission to access this page.", extra_tags='danger')
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)


class EventListView(AttendeeRequiredMixin, ListView):
    model = Event
    template_name = "event_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["registered_event_ids"] = set(
            Registration.objects.filter(attendee=self.request.user).values_list("event_id", flat=True)
        )
        return context

class OrganizerDashboardView(OrganizerRequiredMixin, ListView):
    model = Event
    template_name = "organizer_dashboard.html"

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user).order_by("date")
