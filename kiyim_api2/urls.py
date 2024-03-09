from django.contrib import admin
from django.urls import path, include
from users.routers import router
from users.views import AllDataAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('all_data/', AllDataAPIView.as_view(), name='all_data_api')
]