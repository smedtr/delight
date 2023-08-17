import datetime
from django.shortcuts import redirect, render
from django.urls import reverse

from django.contrib.auth import logout

from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, RecipeRequirementMenuItemForm, ReportDateSelectionForm, PurchaseSearchAddForm

# Create your views here.

def LogOut(request):
    logout(request)
    return redirect("/")

class HomeView(LoginRequiredMixin,TemplateView):
    # 
    template_name = "inventory/home.html"

    def get_context_data(self, *args, **kwargs):
        context = context = super().get_context_data(*args, **kwargs)
        context['menu_items'] = MenuItem.objects.all()
        context['ingredients'] = Ingredient.objects.all()
        context['purchases'] = Purchase.objects.all()        
        return context

class IngredientsView(LoginRequiredMixin,ListView):
    template_name = "inventory/ingredients_list.html"
    model = Ingredient

class NewIngredientView(LoginRequiredMixin,CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientForm

class UpdateIngredientView(LoginRequiredMixin,UpdateView):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = IngredientForm

class MenuView(LoginRequiredMixin,ListView):
    template_name = "inventory/menu_list.html"
    model = MenuItem

class NewMenuItemView(LoginRequiredMixin,CreateView):
    model = MenuItem
    template_name = "inventory/add_menu_item.html"
    form_class = MenuItemForm

class UpdateMenuItemView(LoginRequiredMixin,UpdateView):
    model = MenuItem
    template_name = "inventory/update_menu_item.html"
    form_class = MenuItemForm

class NewRecipeRequirementView(LoginRequiredMixin,CreateView):
    model = RecipeRequirement
    template_name = "inventory/add_recipe_requirement.html"
    form_class = RecipeRequirementForm    

class NewRecipeRequirementToMenuItemView(LoginRequiredMixin,CreateView):
    model = RecipeRequirement
    template_name = "inventory/add_recipe_requirement.html"
    form_class = RecipeRequirementMenuItemForm

    def form_valid(self, form):
        form.instance.menu_item_id = self.kwargs['menu_item']
        return super().form_valid(form)

class UpdateRecipeRequirementView(LoginRequiredMixin,UpdateView):
    model = RecipeRequirement
    template_name = "inventory/update_recipe_requirement.html"
    form_class = RecipeRequirementForm  

class PurchasesView(LoginRequiredMixin,ListView):
    model =Purchase
    template_name = "inventory/purchase_list"

class NewPurchaseView(LoginRequiredMixin,TemplateView):
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

class ReportView(LoginRequiredMixin,TemplateView):
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

def ReportDateSelectionView(request, start_date=datetime.date.today(), end_date=datetime.date.today()):
    
     # If this is a POST request then process the Form data
    if request.method == 'POST':        
        # Create a form instance and populate it with data from the request (binding):
        form = ReportDateSelectionForm(request.POST)        
        # Form is  valid:
        if form.is_valid():                        
            startdate = form.cleaned_data['startdate']
            enddate = form.cleaned_data['enddate']            
            purchases = Purchase.objects.filter(
                timestamp__date__range=(startdate,enddate)  
            )  
            str_startdate=startdate.strftime('%Y-%m-%d')
            str_enddate=enddate.strftime('%Y-%m-%d')            
            my_querystring="%s?start_date=" + str_startdate + "&end_date=" + str_enddate           
            return redirect(my_querystring % reverse('selection_reports'))
        #           
        # Form is not valid:
        if not form.is_valid():  
          ###  <ul class="errorlist"><li>Invalid date - renewal in past</li></ul>                      
          return render(request,"inventory/reports_date_selection.html", {'form':form})

            
    # If this is a GET (or any other method) create the default form.
    else:
        # Try to handle this : http://127.0.0.1:8000/selection_reports/?start_date=2023-08-09&end_date=2023-08-10
        start_date = request.GET.get('start_date', datetime.date.today() )
        end_date = request.GET.get('end_date', datetime.date.today())  
        purchases = Purchase.objects.filter(
            timestamp__date__range=(start_date,end_date)           
        )
           
        form = ReportDateSelectionForm(initial={'startdate': start_date,
                                                'enddate': end_date})
        revenue = 0
        total_cost = 0
        for purchase in purchases:
            revenue += purchase.menu_item.price * purchase.quantity

        for purchase in purchases:
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.unit_price * \
                    recipe_requirement.quantity * \
                    purchase.quantity

                                             
        context = {
            'form': form,
            'purchases' : purchases,
            'revenue' : revenue,
            'purchases' : purchases,
            'revenue' : revenue,
            'total_cost' : total_cost,
            'profit' : revenue - total_cost,
        }           

        return render(request, "inventory/reports_date_selection.html", context)

def PurchaseSearchAddView(request):
    # 
    # If this is a POST request then process the Form data
    if request.method == 'POST':        
        # Create a form instance and populate it with data from the request (binding):
        form = PurchaseSearchAddForm(request.POST)        
        # Form is  valid:
        if form.is_valid():             
            form_search = form.cleaned_data['form_search']
            ###values = Blog.objects.filter(name__contains="Cheddar").values_list("pk", flat=True)
            ###entries = Entry.objects.filter(blog__in=list(values))
            #available_menu_items =[X for X in MenuItem.objects.all() if X.available()]
            available_menu_items = [X for X in MenuItem.objects.filter(title__icontains=form_search) if X.available()]

            context = {
                'form': form,  
                'menu_items': available_menu_items,  
                'menu_items_found': len(available_menu_items),                  
            }              
            return render(request, "inventory/add_search_purchase.html", context)
        #           
        # Form is not valid:
        if not form.is_valid():     
          ###  <ul class="errorlist"><li>Invalid date - renewal in past</li></ul>                      
          return render(request,"inventory/add_search_purchase.html", {'form':form})
          
    # If this is a GET (or any other method) create the default form.
    else:       
        available_menu_items = [X for X in MenuItem.objects.all() if X.available()]            
        form = PurchaseSearchAddForm()        
                                             
        context = {
            'form': form, 
            'menu_items': available_menu_items, 
            'menu_items_found': len(available_menu_items),                    
        }           

        return render(request, "inventory/add_search_purchase.html", context)


