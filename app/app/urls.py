from django.contrib import admin
from django.urls import path, include

from part_1.views import home

urlpatterns = [
    path('', home, name='home'),
    path('blog/', include('blog.urls', namespace='api')),
    path('part1/', include('part_1.urls', namespace='part_1')),
    path('part2/', include('part_2.urls', namespace='part_2')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
