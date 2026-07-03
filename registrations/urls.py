from django.urls import path
from .views import AttendeeDashboardView, RegistrationCreateView

urlpatterns = [
    path("dashboard/", AttendeeDashboardView.as_view(), name="attendee_dashboard"),
    path("<int:event_pk>/register/", RegistrationCreateView.as_view() , name="new_registration"),
]