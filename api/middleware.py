from rest_framework.exceptions import ValidationError
from django.http import JsonResponse

class EnsureUserIdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response