import uuid
from django.db import models

# Create your models here.
# Maybe this would be good to move to mongo in the futue

class Recipe(models.Model):
	# store metadata about a recipe
	id 				= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, db_index=True)
	title 			= models.CharField(max_length=75)
	description 	= models.TextField(blank=True)
	cook_time 		= models.CharField(blank=True, max_length=25)
	serving_portion = models.CharField(blank=True, max_length=50)
	image_link 		= models.URLField(blank=True)
	original_source = models.URLField(blank=True)

	def __str__(self):
		return self.title

class Ingredient(models.Model):
	# 1 recipe to many Ingredients
	id 					= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
	recipe 				= models.ForeignKey('Recipe', on_delete=models.CASCADE, db_index=True)
	name 				= models.CharField(max_length=50)
	quantity 			= models.CharField(blank=True, max_length=25)
	unit_measurement 	= models.CharField(blank=True, max_length=25)

	def __str__(self):
		return self.name


class RecipeStep(models.Model):
	# 1 recipe to many steps
	id 			= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
	recipe 		= models.ForeignKey('Recipe', on_delete=models.CASCADE, db_index=True)
	direction 	= models.TextField()

	def __str__(self):
		return self.direction