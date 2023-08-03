from django.shortcuts import render

from django.views.generic.base import TemplateView
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement

# Create your views here.

class HomeView(TemplateView):
    # 
    template_name = "inventory/home.html"

    def get_context_data(self, *args, **kwargs):
        context = context = super().get_context_data(*args, **kwargs)
        context['menu_items'] = MenuItem.objects.all()
        context['ingredients'] = Ingredient.objects.all()
        context['purchases'] = Purchase.objects.all()        
        return context

