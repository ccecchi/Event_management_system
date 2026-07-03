from django.urls import path
from .views import AttendeeDashboardView

urlpatterns = [
    path("dashboard/", AttendeeDashboardView.as_view(), name="attendee_dashboard"),
]