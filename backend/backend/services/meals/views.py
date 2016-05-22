from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Recipe, Ingredient, RecipeStep
from .serializers import RecipeSerializer, IngredientSerializer, RecipeStepSerializer


class RecipeList(APIView):
	"""
	List all recipes
	"""
	def get(self, request, format=None):
		recipes = Recipe.objects.all()
		serializer = RecipeSerializer(recipes, many=True)
		return Response(serializer.data)


class RecipeDetails(APIView):
	"""
	Pull metadata for a specific recipe
	"""
	def get(self, request, pk, format=None):
		recipe = Recipe.objects.get(id=pk)
		serializer = RecipeSerializer(recipe)
		return Response(serializer.data)


class IngredientsList(APIView):
	"""
	Pull ingredients for a specific recipe
	"""
	def get(self, request, recipe_id, format=None):
		ingredients = Ingredient.objects.filter(recipe=recipe_id)
		serializer = IngredientSerializer(ingredients, many=True)
		return Response(serializer.data)


class RecipeSetList(APIView):
	"""
	Pull directions for a specific recipe
	"""
	def get(self, request, recipe_id, format=None):
		recipe_steps = RecipeStep.objects.filter(recipe=recipe_id)
		serializer = RecipeStepSerializer(recipe_steps, many=True)
		return Response(serializer.data)
