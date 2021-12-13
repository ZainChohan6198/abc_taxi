import simplejson as json
from rest_framework import serializers
from booker.models import Booking, Quotation, AirportPlaces
from booker import icabbi
from booker.enums import BookingStatus, IcabbiStatus
from booker.utils import localize_phone, booking_parser, validate_phone, send_email


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('name', 'icabbi_id', 'phone', 'email', 'notes', 'pickup', 'pickup_ref', 'pickup_date', 'pickup_lat',
                  'pickup_lng', 'dropoff', 'dropoff_ref', 'dropoff_lat', 'dropoff_lng',
                  'vehicle_title', 'vehicle_type', 'vehicle_group', 'pickup_extra', 'created_at', 'payment'
                  )
        read_only_fields = ('icabbi_id', 'created_at', 'payment')

    def create(self, validated_data):
        validated_data['phone'] = validate_phone(validated_data['phone'])

        icabbi_response = icabbi.create_booking(validated_data)

        try:
            data = json.loads(icabbi_response.content)['body']['booking']
        except:
            booking_instance = Booking.objects.create(**validated_data)
            booking_instance.status = BookingStatus.FAILED
            booking_instance.save()
            raise serializers.ValidationError("Booking Failed.")
        booking_instance = Booking.objects.create(**validated_data)
        booking_instance.icabbi_id = data['trip_id']
        booking_instance.name = validated_data['name']
        booking_instance.phone = localize_phone(data['phone'])
        booking_instance.price = round(data['payment']['price'], 2)
        booking_instance.pickup_lat = data['address']['lat']
        booking_instance.pickup_lng = data['address']['lat']
        booking_instance.pickup = data['address']['formatted']
        booking_instance.dropoff_lat = data['destination']['lat']
        booking_instance.dropoff_lng = data['destination']['lat']
        booking_instance.dropoff = data['destination']['formatted']
        booking_instance.icabbi_status = IcabbiStatus[data['status']]
        booking_instance.icabbi_response = data
        booking_instance.status = BookingStatus.SUBMITTED
        booking_instance.save()
        if booking_instance.email:
            send_email({'icabbi_id': booking_instance.icabbi_id, 'pickup': booking_instance.pickup,
                        'dropoff': booking_instance.dropoff, 'vehicle_title': booking_instance.vehicle_title,
                        'name': booking_instance.name, 'phone': booking_instance.phone,
                        'price': format(booking_instance.price, '.2f')}, booking_instance.email)
        return booking_instance

    def to_representation(self, instance):
        response = super().to_representation(instance)
        if not instance.icabbi_response == '':
            booking = booking_parser(instance.icabbi_response, instance)
            return booking


class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = ('price', 'pickup_ref', 'pickup_lat', 'pickup_lng', 'distance', 'estimated_time',
                  'dropoff_ref', 'dropoff_lat', 'dropoff_lng', 'vehicle_type', 'created_at',)
        read_only_fields = ('icabbi_id', 'price', 'distance', 'estimated_time', 'created_at',)

    def create(self, validated_data):
        icabbi_response = icabbi.quote_booking(validated_data)

        try:
            raw_data = json.loads(icabbi_response.content)
            quotes = raw_data['body']['quotes'][0]
        except:
            quotation_instance = Quotation.objects.create(**validated_data)
            quotation_instance.save()
            if json.loads(icabbi_response.content)[
                'message'] == 'This Vehicle group is not available. Please use config/vehiclemap to setup your vehicle mapping.':
                raise serializers.ValidationError(
                    "Selected vehicle is not available please select any other type of vehicle.")
            raise serializers.ValidationError("Quotation Failed.")

        quotation_instance = Quotation.objects.create(**validated_data)
        quotation_instance.price = quotes['price']['price']
        quotation_instance.distance = round(raw_data['body']['distance'] / 1609.34, 2)
        quotation_instance.estimated_time = raw_data['body']['duration_minutes']
        quotation_instance.pickup = raw_data['warnings']['postcode_added']
        quotation_instance.dropoff = raw_data['warnings']['destination_postcode_added']
        quotation_instance.save()
        return quotation_instance


class AirportPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportPlaces
        fields = '__all__'

    def to_representation(self, instance):
        data = super(AirportPlacesSerializer, self).to_representation(instance)
        data['id'] = data['location_ref']
        data.pop('location_ref')
        return data
