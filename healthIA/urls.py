from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('token/', views.obtain_auth_token),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]
