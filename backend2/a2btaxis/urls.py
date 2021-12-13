"""a2btaxis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from accounts.api import ContactViewSet, DisplayViewSet
from booker.api import AddressesViewSet, QuotationViewSet, VehiclesViewSet, AirportPlacesViewSet, VehicleTypesViewSet,\
    BookingViewSet, DriversViewSet

router = DefaultRouter()
path('', RedirectView.as_view(url='/admin')),
router.register(r'contact', ContactViewSet, basename='contact-api')
router.register(r'booking', BookingViewSet, basename='booking-api')
router.register(r'addresses', AddressesViewSet, basename='addresses-api')
router.register(r'quotation', QuotationViewSet, basename='quotation-api')
router.register(r'vehicles', VehiclesViewSet, basename='vehicles-api')
router.register(r'vehicletypes', VehicleTypesViewSet, basename='vehicle-type-api')
router.register(r'airportplaces', AirportPlacesViewSet, basename='airport-api')
router.register(r'drivers', DriversViewSet, basename='driver-api')
router.register(r'show', DisplayViewSet, basename='show-api')


urlpatterns = [

    path('admin/', admin.site.urls),
] + router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
