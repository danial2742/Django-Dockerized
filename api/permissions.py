from rest_framework import permissions
from account.models import License


class LicensePermission(permissions.BasePermission):
	"""
	Global permission check for License.
	"""
	message = 'License is not available.'

	def has_permission(self, request, view):
		return License.objects.valid_license(request.user, License.TYPE_API).exists()
