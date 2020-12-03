import json

class HitCalculatorMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		self.hit_operations(request, response)
		return response
	
	@staticmethod		
	def hit_operations(request, response):
		status_code = response.status_code

		print("status_code: " + str(request))
		print(response)