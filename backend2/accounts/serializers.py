from django.conf import settings
from django.core.mail import send_mail
from rest_framework import serializers
from accounts.models import Contact, Display


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'phone_num', 'email', 'message', 'status')
        read_only_fields = ('status',)

    def create(self, validated_data):
        contact_us = Contact.objects.create(**validated_data)
        subject = validated_data['name']
        message = "Email from : " + validated_data['email'] + '\n '+"Customer Phone Number : " +\
                  validated_data['phone_num'] + '\n' + validated_data['message']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['tasifa123@hotmail.com', ]
        response = send_mail(subject, message, email_from, recipient_list)
        if response == 1:
            contact_us.status = True
        else:
            contact_us.status = False
        contact_us.save()
        return contact_us


class DisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Display
        fields = '__all__'
