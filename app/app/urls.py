from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls', namespace='api')),
    path('demo/', include('demo.urls', namespace='demo')),
    path('admin/', admin.site.urls),
]
