import json

from datetime import timedelta

from django.db.models import Avg, Count
from django.db.models.functions import TruncDay
from django.utils import timezone

from app.models import Exercice, Member, MemberLastActivity, Session

from core.utils.user import User

from social_network.models import Comment, Like, Publication

def format_timedelta(td):
    if not td:
        return "0s"
    total_seconds = int(td.total_seconds())
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}m {seconds}s"

def line_chart(labels, data, data_label):
    return json.dumps({
        "labels": labels,
        "datasets": [
            {
                "label": data_label,
                "data": data,
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

def dashboard_callback(request, context): # pylint: disable=too-many-locals
    now = timezone.now()
    like_day_period = 15
    start_date = (now - timedelta(days=like_day_period - 1)).replace(hour=0, minute=0, second=0, microsecond=0)

    likes_stats = (
        Like.objects.filter(created_at__range=(start_date, now))
        .annotate(day=TruncDay('created_at'))
        .values('day')
        .annotate(count=Count('id'))
        .order_by('day')
    )
    new_members_stats = (
        Member.objects.filter(created_at__date__gte=start_date)
            .values('created_at__date')
            .annotate(total=Count('id'))
    )
    last_activity_stats = (
        MemberLastActivity.objects.filter(date__gte=start_date)
            .values('date')
            .annotate(total=Count('id'))
    )

    labels = []
    likes_map = {item['day'].date(): item['count'] for item in likes_stats}
    new_members_map = {item['created_at__date']: item['total'] for item in new_members_stats}
    last_activity_map = {item['date']: item['total'] for item in last_activity_stats}
    likes = []
    new_members = []
    last_activities = []

    for i in range(like_day_period):
        date = (start_date + timedelta(days=i)).date()
        labels.append(date.strftime("%d %b"))
        likes.append(likes_map.get(date, 0))
        new_members.append(new_members_map.get(date, 0))
        last_activities.append(last_activity_map.get(date, 0))

    context["likes_chart"] = line_chart(labels, likes, "Likes")
    context["new_members_chart"] = line_chart(labels, new_members, "New members")
    context["last_activities_chart"] = line_chart(labels, last_activities, "Members")

    total_pub = Publication.objects.count()
    total_com = Comment.objects.count()

    average = total_com / total_pub if total_pub > 0 else 0
    comment_per_pub = int(average) if average.is_integer() else round(average, 2)

    average_duration = Session.objects.aggregate(avg=Avg('duration'))['avg']
    readable_avg = format_timedelta(average_duration)

    clients = User.objects.filter(members__isnull=True).count()
    members = Member.objects.count()

    context["doughnut_member"] = json.dumps({
        "labels": ["Clients", "Members"],
        "datasets": [{
            "data": [clients, members],
            "backgroundColor": ["#3b82f6", "#10b981"],
            "hoverOffset": 15,
            "borderWidth": 0,
        }],
    })

    free = Member.objects.filter(subscription__value="FREE").count()
    premium = Member.objects.filter(subscription__value="PREMIUM").count()
    premium_plus = Member.objects.filter(subscription__value="PREMIUM PLUS").count()

    context["doughnut_subscription"] = json.dumps({
        "labels": ["Free", "Premium", "Premium Plus"],
        "datasets": [{
            "data": [free, premium, premium_plus],
            "backgroundColor": ["#3b82f6", "#10b981", "#00D68D"],
            "hoverOffset": 15,
            "borderWidth": 0,
        }],
    })

    context["social_network"] = [
        {
            "title": "Total publication",
            "metric": Publication.objects.count(),
        },
        {
            "title": "Comment per publication",
            "metric": ("" if average.is_integer() else "~") + str(comment_per_pub),
        },
    ]

    exercices = Exercice.objects.count()
    stats_exercices = (
        Exercice.objects.values('category__value')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    exercice_labels = [item['category__value'] for item in stats_exercices]
    exercice_counts = [item['total'] for item in stats_exercices]

    context["doughnut_exercice"] = json.dumps({
        "total": exercices,
        "data": {
            "labels": exercice_labels,
            "datasets": [{
                "data": exercice_counts,
                "backgroundColor": ["#10b981", "#3b82f6", "#f59e0b", "#ef4444", "#8b5cf6"],
                "hoverOffset": 15,
                "borderWidth": 0,
            }],
        }
    })

    sessions = Session.objects.count()
    context["doughnut_session"] = json.dumps({
        "labels": ["Sessions"],
        "datasets": [{
            "data": [sessions],
            "backgroundColor": ["#10b981"],
            "hoverOffset": 15,
            "borderWidth": 0,
        }],
    })

    context["coach"] = [
        {
            "title": "Session average time",
            "metric": readable_avg,
        },
    ]

    return context
