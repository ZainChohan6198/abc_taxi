from django.contrib import admin
from booker.models import Booking, Quotation, AirportPlaces


admin.site.register(Quotation)
admin.site.register(AirportPlaces)
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('icabbi_id', 'phone', 'name', 'dropoff', 'icabbi_status',)
    search_fields = ('name', 'phone',)
    fields = ['icabbi_id', 'name', 'phone', 'pickup', 'dropoff','pickup_date', 'icabbi_status', 'icabbi_response']
