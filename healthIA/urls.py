from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from app.views.users import UserViewSet
from app.views.dataset import DataImportViewSet
from app.views.members import MemberViewSet
from app.views.exercices import ExerciceViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'import', DataImportViewSet, basename='import')
router.register(r'members', MemberViewSet, basename='members')
router.register(r'exercices', ExerciceViewSet, basename='exercices')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', views.obtain_auth_token),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]
