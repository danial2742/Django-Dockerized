from account.models import license

class HitCalculatorMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)

		if request.path.startswith('/api/') and 200 <= response.status_code < 300:
			self.license_increment(request, 1)

		return response

	@staticmethod
	def license_increment(request, count):
		license.objects.add_used_count(request.user, license.TYPE_API, count)

