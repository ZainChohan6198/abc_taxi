import jsonfield
from django.db import models
from enumfields import EnumField
from booker import enums


class Booking(models.Model):
    icabbi_id = models.CharField(max_length=120, null=True, blank=True)
    name = models.CharField(max_length=120, null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=70, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    price = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)

    pickup = models.CharField(max_length=120, blank=True)
    pickup_ref = models.CharField(max_length=120)
    pickup_lat = models.CharField(max_length=20, blank=True, null=True)
    pickup_lng = models.CharField(max_length=20, blank=True, null=True)
    pickup_date = models.DateTimeField(blank=True, null=True)

    dropoff = models.CharField(max_length=120, blank=True)
    dropoff_ref = models.CharField(max_length=120)
    dropoff_lat = models.CharField(max_length=20, blank=True, null=True)
    dropoff_lng = models.CharField(max_length=20, blank=True, null=True)

    payment = EnumField(enums.PaymentType, default=enums.PaymentType.CASH, max_length=120)
    vehicle_title = models.CharField(max_length=20, null=True, blank=True)
    vehicle_type = models.CharField(max_length=20, null=True, blank=True)
    vehicle_group = models.CharField(max_length=20, null=True, blank=True)
    status = EnumField(enums.BookingStatus, default=enums.BookingStatus.PENDING, max_length=120)
    icabbi_status = EnumField(enums.IcabbiStatus, default=enums.IcabbiStatus.NEW, max_length=120)
    created_at = models.DateTimeField(auto_now=True)
    pickup_extra = models.CharField(max_length=120, null=True, blank=True)
    icabbi_response = jsonfield.JSONField()

    def __str__(self):
        return self.name


class Quotation(models.Model):
    price = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    pickup = models.CharField(max_length=120, null=True, blank=True)
    pickup_ref = models.CharField(max_length=120)
    pickup_lat = models.CharField(max_length=20)
    pickup_lng = models.CharField(max_length=20)
    dropoff = models.CharField(max_length=20, null=True, blank=True)
    dropoff_ref = models.CharField(max_length=120)
    dropoff_lat = models.CharField(max_length=20)
    dropoff_lng = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=20)
    distance = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    estimated_time = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pickup_ref


class AirportPlaces(models.Model):
    name = models.CharField(max_length=120, null=True)
    location_ref = models.CharField(max_length=120, null=True, blank=True)
    formatted = models.CharField(max_length=120, null=True, blank=True)
    lat = models.CharField(max_length=20, null=True, blank=True)
    lng = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
