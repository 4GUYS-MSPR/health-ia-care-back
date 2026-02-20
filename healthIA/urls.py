from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from app.views import ExerciceViewSet, MemberViewSet, SessionViewSet

from core.views import DataImportViewSet, EnumViewSet, UserViewSet

from logs.views import LogViewSet

from nutrition.views import DietRecommendationViewSet, FoodViewSet

router = routers.DefaultRouter()
router.register(r'diet_recommendation', DietRecommendationViewSet, basename='diet_recommendation')
router.register(r'enum', EnumViewSet, basename='enum')
router.register(r'exercice', ExerciceViewSet, basename='exercice')
router.register(r'food', FoodViewSet, basename='food')
router.register(r'import', DataImportViewSet, basename='import')
router.register(r'log', LogViewSet, basename='log')
router.register(r'member', MemberViewSet, basename='member')
router.register(r'session', SessionViewSet, basename='session')
router.register(r'user', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', views.obtain_auth_token),
    path('api/token-jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]
