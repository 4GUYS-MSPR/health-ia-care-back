from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('token/', views.obtain_auth_token),
]
