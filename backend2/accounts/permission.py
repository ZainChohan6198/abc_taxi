from django.conf import settings
from django.db.backends.utils import logger
from rest_framework import permissions


class WhitelistPermission(permissions.BasePermission):
    """
    Global permission check for whitelisted IPs.
    """

    def has_permission(self, request, view):
        ip_addr = request.META.get('REMOTE_ADDR')
        domain = request.META.get('HTTP_ORIGIN')
        if ip_addr in settings.WHITELIST_API:
            return True
        return False
