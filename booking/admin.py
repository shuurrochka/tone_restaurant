from django.contrib import admin
from .models import TableBooking

@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'time', 'guests')
    search_fields = ('name', 'phone')