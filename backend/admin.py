from django.contrib import admin
from .models import FoodItem  # Import your model
# Register your models here.

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'food_category', 'expected_shelf_life', 'expected_fridge_life', 'expected_freezer_life', 'default_storage_method')
    # Add other fields as needed in the order you want them to appear

admin.site.register(FoodItem, FoodItemAdmin)
# admin.site.register(FoodItem)
