from rest_framework import viewsets, status
from accounts.models import Contact, Display
from accounts.serializers import ContactSerializer, DisplaySerializer
from accounts.permission import WhitelistPermission


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [WhitelistPermission]


class DisplayViewSet(viewsets.ModelViewSet):
    queryset = Display.objects.all()
    serializer_class = DisplaySerializer
    permission_classes = [WhitelistPermission]

    def get_queryset(self):
        queryset = Display.objects.filter()[:1]
        return queryset
