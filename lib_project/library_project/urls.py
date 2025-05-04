from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library_app.views import BookViewSet, BookingViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'bookings', BookingViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Library API",
        default_version='v1',
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]
