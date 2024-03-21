from rest_framework import routers
from .views import TruckViewSet, CargoViewSet

router = routers.DefaultRouter()
router.register(r'truck', TruckViewSet)
router.register(r'cargo', CargoViewSet)