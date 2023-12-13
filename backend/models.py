from django.db import models

# Create your models here.

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    food_category = models.CharField(max_length=50)
    expected_shelf_life = models.IntegerField()
    expected_fridge_life = models.IntegerField()
    expected_freezer_life = models.IntegerField()
    default_storage_method = models.CharField(max_length=50)

    def __str__(self):
        return self.name