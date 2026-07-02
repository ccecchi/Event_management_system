from django.urls import path
from .views import OrganizerDashboardView, EventCreateView

urlpatterns = [
    path("dashboard/", OrganizerDashboardView.as_view(), name="organizer_dashboard"),
    path("create/", EventCreateView.as_view(), name="new_event"),
]