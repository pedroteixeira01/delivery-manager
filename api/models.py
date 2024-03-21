from django.db import models

class Truck(models.Model):
    truck = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=4)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Cargo(models.Model):
    product = models.CharField(max_length=200)
    origin_city = models.CharField(max_length=200)
    origin_state = models.CharField(max_length=4)
    origin_latitude = models.FloatField()
    origin_longitude = models.FloatField()
    destination_city = models.CharField(max_length=200)
    destination_state = models.CharField(max_length=4)
    destination_latitude = models.FloatField()
    destination_longitude = models.FloatField()