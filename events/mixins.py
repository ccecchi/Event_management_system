from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Event

class EventOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        self.event = get_object_or_404(Event, pk=kwargs.get("pk"))
        if request.user != self.event.organizer:
            messages.error(request, "You do not have permission to access this page.", extra_tags='danger')
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)