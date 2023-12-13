# yourapp/management/commands/import_fooditems.py
import csv
from django.core.management.base import BaseCommand
from backend.models import FoodItem

class Command(BaseCommand):
    help = 'Import food items from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import')

    def handle(self, *args, **kwargs):
        file_path = kwargs['csv_file']
        FoodItem.objects.all().delete()  # Deletes all existing records in FoodItem

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                FoodItem.objects.create(
                    name=row['name'],
                    food_category=row['foodCategory'],
                    expected_shelf_life=int(row['expectedShelfLife']),
                    expected_fridge_life=int(row['expectedFridgeLife']),
                    expected_freezer_life=int(row['expectedFreezerLife']),
                    default_storage_method=row['defaultStorageMethod']
                )
