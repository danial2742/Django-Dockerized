from rest_framework import permissions
from account.models import license

class LicensePermission(permissions.BasePermission):
	"""
	Global permission check for blocked IPs.
	"""
	message = 'License is not available.'

	def has_permission(self, request, view):
		has_license = license.objects.valid_license(request.user).exists();
		return has_license