from rest_framework import viewsets
from .models import Truck, Cargo
from .serializers import TruckSerializer, CargoSerializer


class TruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer