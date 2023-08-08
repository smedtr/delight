from django.shortcuts import redirect

from django.db.models import Sum
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, RecipeRequirementMenuItemForm, PurchaseForm, PurchaseMultiMenuItemForm

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

class NewPurchaseView(TemplateView):
    # 
    template_name = "inventory/add_purchase.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # De menu_items die we tonen zijn alleen de menu_items die available zijn
        context['menu_items'] =[X for X in MenuItem.objects.all() if X.available()]              
        return context
    
    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        qty_purchased = float(request.POST["quantity"])
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item,quantity=qty_purchased)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= (requirement.quantity*qty_purchased) 
            required_ingredient.save()

        purchase.save()
        return redirect("/purchases")

class ReportView(TemplateView):
    template_name = "inventory/reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = 0
        total_cost = 0
        
        #revenue = Purchase.objects.aggregate(
        #    revenue=Sum("menu_item__price"))["revenue"]
            
        for purchase in Purchase.objects.all():
            revenue += purchase.menu_item.price * purchase.quantity

        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.unit_price * \
                    recipe_requirement.quantity * \
                    purchase.quantity

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context
