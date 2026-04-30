from django.utils import timezone

from app.models import Member, MemberLastActivity

class LastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            try:
                members = Member.objects.filter(user=request.user)
                if len(members) == 0 or len(members) > 1:
                    raise Member.DoesNotExist('No matching query' if len(members) == 0 else 'To many members')

                member = members[0]
                member.last_activity = timezone.now()
                member.save()

                today = timezone.now().date()
                MemberLastActivity.objects.get_or_create(
                    member=member,
                    date=today
                )
            except Member.DoesNotExist:
                pass

        return response
