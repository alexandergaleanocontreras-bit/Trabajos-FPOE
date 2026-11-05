from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from academico.views.gorra_viewset import GorraViewSet

router = DefaultRouter()
router.register(r'gorras', GorraViewSet, basename='gorra')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]