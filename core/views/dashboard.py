from app.models import Member

from social_network.models import Publication, Comment

def dashboard_callback(request, context):
    context["kpis"] = [
        {
            "title": "members",
            "metric": Member.objects.count(),
        },
        {
            "title": "publications",
            "metric": Publication.objects.count(),
        },
        {
            "title": "comments",
            "metric": Comment.objects.count(),
        },
    ]

    return context
