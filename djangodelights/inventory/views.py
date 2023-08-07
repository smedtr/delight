from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, RecipeRequirementMenuItemForm, PurchaseForm

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

class IngredientsView(ListView):
    template_name = "inventory/ingredients_list.html"
    model = Ingredient

class NewIngredientView(CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientForm

class UpdateIngredientView(UpdateView):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = IngredientForm

class MenuView(ListView):
    template_name = "inventory/menu_list.html"
    model = MenuItem

class NewMenuItemView(CreateView):
    model = MenuItem
    template_name = "inventory/add_menu_item.html"
    form_class = MenuItemForm

class UpdateMenuItemView(UpdateView):
    model = MenuItem
    template_name = "inventory/update_menu_item.html"
    form_class = MenuItemForm

class NewRecipeRequirementView(CreateView):
    model = RecipeRequirement
    template_name = "inventory/add_recipe_requirement.html"
    form_class = RecipeRequirementForm    

class NewRecipeRequirementToMenuItemView(CreateView):
    model = RecipeRequirement
    template_name = "inventory/add_recipe_requirement.html"
    form_class = RecipeRequirementMenuItemForm

    def form_valid(self, form):
        form.instance.menu_item_id = self.kwargs['menu_item']
        return super().form_valid(form)

class UpdateRecipeRequirementView(UpdateView):
    model = RecipeRequirement
    template_name = "inventory/update_recipe_requirement.html"
    form_class = RecipeRequirementForm  

class PurchasesView(ListView):
    model =Purchase
    template_name = "inventory/purchase_list"

class NewPurchaseView(CreateView):
    model = Purchase
    template_name = "inventory/add_purchase.html"
    form_class = PurchaseForm 

