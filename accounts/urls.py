from django.urls import path

from .views import MyLoginView, signup_view

urlpatterns = [
    path("signup/attendee", signup_view, {"role_type": "A"}, name="signup_attendee"),
    path("signup/organizer", signup_view, {"role_type": "O"}, name="signup_organizer"),
    path("login", MyLoginView.as_view(), name="login"),
]