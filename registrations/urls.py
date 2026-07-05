from django.urls import path
from .views import AttendeeDashboardView, RegistrationCreateView, RegistrationDeleteView, RegistrationList

urlpatterns = [
    path("dashboard/", AttendeeDashboardView.as_view(), name="attendee_dashboard"),
    path("<int:event_pk>/register/", RegistrationCreateView.as_view() , name="new_registration"),
    path("<int:pk>/delete/", RegistrationDeleteView.as_view(), name="registration_delete"),
    path("<int:pk>/attendees/", RegistrationList.as_view(), name="attendee_list"),
]