from django.utils import timezone
from app.models import Member

class LastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            Member.objects.filter(user=request.user).update(last_activity=timezone.now())

        return response
