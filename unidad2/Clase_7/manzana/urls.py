from rest_framework.routers import DefaultRouter

from manzana.views import ManzanaViewSet

router = DefaultRouter()
router.register("manzanas", ManzanaViewSet, basename="manzana")

urlpatterns = router.urls