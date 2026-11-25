from rest_framework.routers import DefaultRouter

from .views import ManzanaViewSet

router = DefaultRouter()
router.register("manzanas", ManzanaViewSet)

urlpatterns = router.urls
