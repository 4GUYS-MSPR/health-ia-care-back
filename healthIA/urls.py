from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from app.serializers.user import UserViewSet
from app.views.dataset import DataImportViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'import', DataImportViewSet, basename='import')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', views.obtain_auth_token),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]
