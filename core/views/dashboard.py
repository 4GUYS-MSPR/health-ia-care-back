import json

from datetime import timedelta

from django.db.models import Avg, Count
from django.db.models.functions import TruncDay
from django.utils import timezone

from app.models import Member, Session

from social_network.models import Comment, Like, Publication

def format_timedelta(td):
    if not td:
        return "0s"
    total_seconds = int(td.total_seconds())
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}m {seconds}s"

def dashboard_callback(request, context): # pylint: disable=too-many-locals
    now = timezone.now()
    last_24h = now - timedelta(hours=24)

    like_day_period = 15
    start_date = (now - timedelta(days=like_day_period - 1)).replace(hour=0, minute=0, second=0, microsecond=0)

    likes_per_day = (
        Like.objects.filter(created_at__range=(start_date, now))
        .annotate(day=TruncDay('created_at'))
        .values('day')
        .annotate(count=Count('id'))
        .order_by('day')
    )

    data_map = {item['day'].date(): item['count'] for item in likes_per_day}
    labels = []
    values = []

    for i in range(like_day_period):
        date = (start_date + timedelta(days=i)).date()
        labels.append(date.strftime("%d %b"))
        values.append(data_map.get(date, 0))

    new_members_24h = Member.objects.filter(created_at__gte=last_24h).count()

    context["likes_chart"] = json.dumps({
        "labels": labels,
        "datasets": [
            {
                "label": "Likes",
                "data": values,
                "borderColor": "#059669",
                "backgroundColor": "#059669",
                "borderWidth": 3,
                "pointRadius": 0,
                "pointHoverRadius": 6,
                "tension": 0,
            }
        ],
        "options": {
            "responsive": True,
            "maintainAspectRatio": False,
            "interaction": {
                "intersect": False,
                "mode": 'index',
            },
            "plugins": {
                "legend": {"display": False},
                "tooltip": {
                    "enabled": True,
                    "backgroundColor": "#1e293b",
                    "titleColor": "#fff",
                    "bodyColor": "#fff",
                    "padding": 10,
                }
            },
            "scales": {
                "x": {
                    "display": True,
                    "grid": {
                        "display": True,
                        "drawBorder": False,
                        "borderDash": [5, 5],
                        "color": "rgba(156, 163, 175, 0.2)",
                    },
                    "ticks": {
                        "color": "#9ca3af",
                        "font": {"size": 11},
                    }
                },
                "y": {
                    "display": True,
                    "beginAtZero": True,
                    "grid": {
                        "display": True,
                        "drawBorder": False,
                        "borderDash": [5, 5],
                        "color": "rgba(156, 163, 175, 0.2)",
                    },
                    "ticks": {
                        "color": "#9ca3af", 
                        "font": {"size": 11},
                        "precision": 0,
                    }
                }
            }
        }
    })

    total_pub = Publication.objects.count()
    total_com = Comment.objects.count()

    average = total_com / total_pub if total_pub > 0 else 0
    comment_per_pub = int(average) if average.is_integer() else round(average, 2)

    average_duration = Session.objects.aggregate(avg=Avg('duration'))['avg']
    readable_avg = format_timedelta(average_duration)

    context["kpis"] = [
        {
            "title": "Total members",
            "metric": Member.objects.count(),
        },
        {
            "title": "New Members (24h)",
            "metric": f"+ {new_members_24h}",
        },
        {
            "title": "Member connected (24h)",
            "metric": Member.objects.filter(last_activity__gte=last_24h).count(),
        },
        {
            "title": "Session average time",
            "metric": readable_avg,
        },
        {
            "title": "Comment per publication",
            "metric": f"{"" if average.is_integer() else "~"} {comment_per_pub}",
        },
    ]

    return context
