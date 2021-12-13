import simplejson as json
import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings
from booker.utils import validate_phone


def icabbi_request(method, endpoint, data):
    auth = HTTPBasicAuth(settings.ICABBI_USERNAME, settings.ICABBI_PASSWORD)
    response = {}
    if method == 'GET':
        response = requests.get(settings.ICABBI_SERVER + endpoint, params=data, auth=auth)
    elif method == 'POST':
        response = requests.post(settings.ICABBI_SERVER + endpoint, data=data, auth=auth)
    return response


def get_booking(args):
    ''' get booking using trip id '''

    booking = icabbi_request('GET', 'bookings/index/{0}'.format(args), {})

    return booking


def get_bookings(args):
    ''' get bookings using phone no '''
    data = {
        "passenger_phone": args,
        "status": "EN_ROUTE",
        "direction": "DESC",
        "order": "pickup_date",
    }

    booking = icabbi_request('GET', '/bookings/history', data)

    return booking


def cancel_booking(args):
    ''' cancel booking using trip id '''

    booking = icabbi_request('POST', 'bookings/cancel/{0}'.format(args), {})

    return booking


def get_user_addresses(phone):
    ''' get user addresses using phone number '''
    data = {
        'phone': validate_phone(phone),
        'used': 1,
        'period': 500
    }
    addresses = icabbi_request('GET', 'users/addresses/', data)

    return addresses


def get_addresses(query):
    ''' search for addresses using a query '''
    data = {
        'query': query,
        'formatted': 1,
        'geo': 1}

    addresses = icabbi_request('GET', 'addresses/search?', data)

    return addresses


def get_address(id):
    ''' using query search addresses'''
    addresses = icabbi_request('GET', 'addresses/view/{0}'.format(id), {})

    return addresses


def get_driver_by_position():
    ''' fetch all the drivers'''

    drivers = icabbi_request('GET', 'drivers/positions',{})
    try:
        drivers = json.loads(drivers.content)['body']['positions']
    except:
        drivers = None

    return drivers


def get_driver_by_id(id):
    ''' Update all the driver using indexes '''

    response = icabbi_request('GET', 'drivers/index/' + str(id), {})
    try:
        driver = json.loads(response.content)['body']['driver']
    except:
        driver = None
    return driver


def get_vehicles():
    ''' get vehicles of API'''
    vehicles = icabbi_request('GET', 'vehicle', {})

    return vehicles


def get_vehicle_types():
    ''' get vehicle types of API'''
    vehicle_type = icabbi_request('GET', 'config/vehicletypes', {})

    return vehicle_type


def create_booking(validated_data):
    data = {
        'source': 'WEB',
        'name': validated_data.get('name'),
        'instructions': validated_data.get('notes'),
        'phone': validated_data.get('phone'),
        'address': {
            'lat': 1,
            'lng': 1,
            'formatted': '',
            'id': validated_data.get('pickup_ref')
        },
        'destination': {
            'lat': 1,
            'lng': 1,
            'formatted': '',
            'id': validated_data.get('dropoff_ref'),
            'pickup_extra': validated_data.get('pickup_extra')
        },
        'vehicle_type': validated_data.get('vehicle_type'),
        'vehicle_group': validated_data.get('vehicle_group'),
    }

    if validated_data.get('pickup_date'):
        data['date'] = validated_data.get('pickup_date').isoformat()

    booking = icabbi_request('POST', 'bookings/add/', data=json.dumps(data))
    return booking


def quote_booking(validated_data):
    data = {
        "address_id": validated_data.get('pickup_ref'),
        "destination_id": validated_data.get('dropoff_ref'),
        "locations": [
            validated_data.get('pickup_lat') + "," + validated_data.get('pickup_lng'),
            validated_data.get('dropoff_lat') + "," + validated_data.get('dropoff_lng'),
        ],
        "vehicle_group": validated_data.get('vehicle_type'),
    }

    quotation = icabbi_request('POST', 'quote', data=json.dumps(data))
    return quotation
