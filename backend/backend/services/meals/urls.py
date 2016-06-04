from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RecipeList, RecipeDetails, IngredientsList, RecipeSetList

urlpatterns = [
	url(r'^recipes/$', RecipeList.as_view()),
	url(r'^recipe/(?P<pk>[0-9a-z-]+)/$', RecipeDetails.as_view()),
	url(r'^ingredients/(?P<recipe_id>[0-9a-z-]+)/$', IngredientsList.as_view()),
	url(r'^directions/(?P<recipe_id>[0-9a-z-]+)/$', RecipeSetList.as_view()),
]

# allows us to manage different content types i.e. json, html etc 
urlpatterns = format_suffix_patterns(urlpatterns)
