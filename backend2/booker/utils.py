from django.conf import settings
from django.core.mail import send_mail
from django.db.backends.utils import logger
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from booker.models import Booking


def status_parser(status):
    if status == 'NEW' or status == 'PAUSED':
        status = 'Waiting for driver'
    elif status == 'CUSTOMER_CANCELLED' or status == 'DRIVER_CANCELLED' or status == 'DISPATCH_CANCELLED':
        status = 'Cancelled'
    elif status == 'ASSIGN' or status == 'WAIT':
        status = 'Assigned to driver'
    elif status == 'MADECONTACT' or status == 'ENROUTE':
        status = 'Driver is on the way'
    elif status == 'COMPLETED':
        status = 'Completed'
    elif status == 'DROPPINGOFF':
        status = 'Dropping off'
    elif status == 'NOSHOW':
        status = 'No Show'
    elif status == 'ARRIVED':
        status = 'Driver arrived'
    return status


def booking_parser(booking, instance=None):
    if not instance:
        instance = Booking.objects.get(icabbi_id=booking['trip_id'])

    response = {
        'id': booking['trip_id'],
        'eta': booking['eta'],
        'name': instance.name,
        'phone': instance.phone,
        'created_date': booking['created_date'],
        'pickup_date': booking['pickup_date'],
        'price': booking['payment']['price'],
        'pickup': booking['address'],
        'dropoff': booking['destination'],
        'vehicle': booking['vehicle_type'],
        'vehicle_title': instance.vehicle_title,
        'notes': booking['instructions'],
        'email': instance.email,
        'status_text': booking['status_text'],
        'pickup_extra': instance.pickup_extra,
        'icabbi_status': status_parser(booking['status']),
        'booking_status': instance.status.name,
        'payment': instance.payment.name,
        'driver_id': booking['driver_id']
    }
    return response


def bookings_parser(bookings):
    bookings_response = []
    for booking in reversed(bookings):
        response = {
            'id': booking['trip_id'],
            'eta': booking['eta'],
            'name': booking['name'],
            'phone': booking['phone'],
            'created_date': booking['created_date'],
            'pickup_date': booking['pickup_date'],
            'price': booking['payment']['price'],
            'pickup': booking['address'],
            'dropoff': booking['destination'],
            'vehicle': booking['vehicle_type'],
            'notes': booking['instructions'],
            'status_text': booking['status_text'],
            'pickup_extra': booking['address']['formatted'],
            'driver_id': booking['driver']['id'],
        }
        bookings_response.append(response)
    return bookings_response


def addresses_parser(addresses):
    searched_addresses = []
    for address in addresses:
        search_item = {
            'id': address['id'],
            'formatted': address['formatted'],
            'lat': address['lat'],
            'lng': address['lng'],
        }
        searched_addresses.append(search_item)
    return searched_addresses


def validate_phone(phone):
    if phone.startswith('007'):
        phone = phone[1:]
    if phone.startswith('07') and len(phone) >= 10:
        phone = '0044' + ''.join(list(phone)[1:])
    elif not phone.startswith('00') and len(phone) >= 9:
        phone = '0044' + ''.join(list(phone))
    elif len(phone) < 9:
        phone = None
    return phone


def localize_phone(phone):
    if phone.startswith('0044'):
        return '0'+phone[4:]
    return phone


def send_email(booking_data, email):
    html_message = render_to_string('index.html',  booking_data)

    mail_data = {
        "subject": 'Booking Info',
        "html_message": html_message,
        "recipient_list": [email],
        "from_email": settings.EMAIL_HOST_USER,
        'message': strip_tags(html_message)
    }
    try:
        send_mail(**mail_data)
        logger.debug('Email is sent on {} '.format(email))
    except Exception as e:
        logger.debug('Email is not sent on {} '.format(email))
