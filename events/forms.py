from django import forms
from .models import Event
from django.utils import timezone

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("title", "date", "address", "capacity", "descr")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "date": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "capacity": forms.NumberInput(attrs={"class": "form-control"}),
            "descr": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def clean_date(self):
        date = self.cleaned_data.get("date")
        if date and date < timezone.now():
            raise forms.ValidationError("The event date can't be in the past.")
        return date