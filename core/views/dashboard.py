from app.models import Member
from social_network.models import Publication, Comment

def dashboard_callback(request, context):
    context["kpis"] = [
        {
            "title": "Members",
            "metric": Member.objects.count(),
        },
        {
            "title": "Publications",
            "metric": Publication.objects.count(),
        },
        {
            "title": "Comments",
            "metric": Comment.objects.count(),
        },
    ]

    return context
