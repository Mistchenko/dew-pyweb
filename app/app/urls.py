from django.contrib import admin
from django.urls import path, include

from part_1.views import home

urlpatterns = [
    path('', home, name='home'),
    path('blog/', include('blog.urls', namespace='api')),
    path('demo/', include('demo.urls', namespace='demo')),
    path('admin/', admin.site.urls),
]
