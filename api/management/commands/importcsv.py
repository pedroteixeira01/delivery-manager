import csv
from django.core.management.base import BaseCommand
from api.models import Truck, Cargo

class Command(BaseCommand):
    help = 'Import data from a Truck and Cargo CSV file into the database'
    
    def add_arguments(self, parser):
        parser.add_argument("--truck", type=str, help="csv file that contains the trucks")
        parser.add_argument("--cargo", type=str, help="csv file that contains the cargos")

    def handle(self, *args, **options):
        if options["truck"] != None:
            with open(options["truck"], 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skips the header row
            
                for row in reader:
                    Truck.objects.create(truck=row[0], city=row[1], state=row[2], latitude=row[3], longitude=row[4])
        
        if options["cargo"] != None:
            with open(options["cargo"], 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skips the header row
            
                for row in reader:
                    Cargo.objects.create(product=row[0], origin_city=row[1], origin_state=row[2], origin_latitude=row[3], origin_longitude=row[4], destination_city=row[5], destination_state=row[6], destination_latitude=row[7], destination_longitude=row[8])
        
        if options["cargo"] != None or options["truck"] != None:
            self.stdout.write(self.style.SUCCESS('Imported data from CSV files.'))
