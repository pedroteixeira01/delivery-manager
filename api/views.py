from rest_framework import viewsets
from django.http import JsonResponse
from .models import Truck, Cargo
from .serializers import TruckSerializer, CargoSerializer
from geopy import distance as geo


class TruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


def MappingView(request):
    trucks = Truck.objects.all()
    cargos = Cargo.objects.all()
    result = []
    chosen = []

    for cargo in cargos:
        closest_truck = 'No available truck'
        shortest_distance = 10000000
        point1 = (cargo.origin_latitude, cargo.origin_longitude)

        for truck in trucks:
            point2 = (truck.latitude, truck.longitude)
            distance = geo.distance(point1, point2).km

            if ( (distance < shortest_distance) and (truck.truck not in chosen) ):
                shortest_distance = distance
                closest_truck = truck.truck
                chosen.append(truck.truck)
        result.append(
            {
                'truck_name': closest_truck,
                'cargo_name': cargo.product,
                'distance': round(shortest_distance, 2)
            }
        )

    return JsonResponse(result, safe=False)