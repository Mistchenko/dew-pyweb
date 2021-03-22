from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('blog.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
