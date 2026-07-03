from django.urls import path
from .views import OrganizerDashboardView, EventCreateView, EventDetailView, EventDeleteView, EventUpdateView, EventListView

urlpatterns = [
    path("<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("dashboard/", OrganizerDashboardView.as_view(), name="organizer_dashboard"),
    path("create/", EventCreateView.as_view(), name="new_event"),
    path("<int:pk>/delete/", EventDeleteView.as_view(), name="event_delete"),
    path("<int:pk>/edit/", EventUpdateView.as_view(), name="event_edit"),
    path("", EventListView.as_view(), name="event_list"),
]