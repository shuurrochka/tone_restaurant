from django import forms
from .models import TableBooking

class BookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ['name', 'phone', 'date', 'time', 'guests']