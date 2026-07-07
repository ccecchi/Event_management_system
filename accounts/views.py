from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.contrib import messages


def signup_view(request: HttpRequest, role_type="A") -> HttpResponse:
    if request.user.is_authenticated:
        messages.info(request, "You are already registered and logged in.")
        return redirect("home")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = role_type
            user.save()
            messages.success(request, f'Account for "{user.username}" has been successfully created!')
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(request, "signup.html", {"form": form, "role_type": role_type})


class MyLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in.")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        if self.request.user.is_organizer():
            return reverse_lazy("organizer_dashboard")
        return reverse_lazy("attendee_dashboard")