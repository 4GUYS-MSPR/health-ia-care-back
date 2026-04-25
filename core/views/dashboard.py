from app.models import Member

from logs.models import Log

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
        {
            "title": "requests",
            "metric": Log.objects.count(),
        },
    ]

    context["logs"] = {
        "collapsible": True,
        "headers": ["Level", "Method", "Path", "User"],
        "rows": [
            {
                "level": log.level,
                "method": log.method,
                "path": log.path,
                "user": log.user.username if log.user is not None else "Anonymous",
            } for log in Log.objects.order_by('-created_at')[:30]
        ]
    }

    return context
