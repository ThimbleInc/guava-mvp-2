from rest_framework import serializers
from .models import Recipe, Ingredient, RecipeStep


class RecipeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recipe
		fields = ('id','description', 'title','cook_time', 'serving_portion', 'image_link', 'original_source')

class IngredientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ingredient
		fields = ('id', 'recipe', 'name', 'quantity', 'unit_measurement')

class RecipeStepSerializer(serializers.ModelSerializer):
	class Meta:
		model = RecipeStep
		fields = ('id', 'recipe', 'direction')