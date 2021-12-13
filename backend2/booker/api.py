import simplejson as json
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import Http404
from accounts.permission import WhitelistPermission
from booker.models import Booking, Quotation, AirportPlaces
from booker.serializers import AirportPlacesSerializer, QuotationSerializer, BookingSerializer
from booker.utils import addresses_parser, validate_phone, localize_phone, booking_parser
from booker.icabbi import cancel_booking, get_booking, get_addresses, get_user_addresses, get_vehicles, \
    get_vehicle_types, get_driver_by_position, get_driver_by_id


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [WhitelistPermission]

    def get_queryset(self):
        return Booking.objects.all()

    def retrieve(self, request, *args, **kwargs):
        icabbi_id = kwargs.get('pk')
        raw_response = get_booking(args=icabbi_id)
        try:
            booking = json.loads(raw_response.content)['body']['booking']
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = booking_parser(booking)
        if not response['driver_id'] == '0' and response['driver_id']:
            response['driver'] = get_driver_by_id(response['driver_id'])
            driver_positions = get_driver_by_position()
            driver_position = list(filter(lambda driver: driver['id'] == int(response['driver_id']), driver_positions))
            response['driver']['position'] = driver_position[0] if driver_position else {}

        return Response(response, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        booking_response = cancel_booking(args=kwargs.get('pk'))
        booking = json.loads(booking_response.content)['code']
        if booking == '0':
            Booking.objects.filter(icabbi_id=kwargs.get('pk')).update(status='CANCELLED',
                                                                      icabbi_status='CUSTOMER_CANCELLED')
            return Response({'data': {'cancel': True}}, status=status.HTTP_200_OK)
        return Response({'data': {'cancel': False}}, status=status.HTTP_404_NOT_FOUND)


class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer
    permission_classes = [WhitelistPermission]


class AirportPlacesViewSet(viewsets.ModelViewSet):
    queryset = AirportPlaces.objects.all()
    serializer_class = AirportPlacesSerializer
    permission_classes = [WhitelistPermission]

    def list(self, request):
        queryset = AirportPlaces.objects.all()
        serializer = AirportPlacesSerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class AddressesViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Address.
    """

    def list(self, request, *args, **kwargs):
        if self.request.GET.get('query'):
            raw_response = get_addresses(query=self.request.query_params['query'])
            try:
                response = json.loads(raw_response.content)['body']['addresses']
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            searched_addresses = addresses_parser(response)
            return Response({'data': searched_addresses}, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = [WhitelistPermission]

        return [permission() for permission in permission_classes]


class VehiclesViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving vehicles.
    """

    def list(self, request):
            raw_response = get_vehicles()
            try:
                response = json.loads(raw_response.content)['body']['vehicles']
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            return Response({'data': response[:10]}, status=status.HTTP_200_OK)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = [WhitelistPermission]

        return [permission() for permission in permission_classes]


class DriversViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving drivers.
    """

    def list(self, request):
            response = get_driver_by_position()
            return Response({'data': response}, status=status.HTTP_200_OK)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = [WhitelistPermission]

        return [permission() for permission in permission_classes]


class VehicleTypesViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving vehicle types.
    """

    def list(self, request):
            raw_response = get_vehicle_types()
            try:
                response = json.loads(raw_response.content)['body']['vehicletypes']
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            return Response({'data': response}, status=status.HTTP_200_OK)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = [WhitelistPermission]

        return [permission() for permission in permission_classes]

