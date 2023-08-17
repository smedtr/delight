from django.urls import path, register_converter
from django.contrib.auth import views as auth_views

from . import views
from .converters import DateConverter

register_converter(DateConverter, 'date')

# selection_reports http://127.0.0.1:8000/selection_reports/?start_date=2023-08-09&end_date=2023-08-10
#
urlpatterns = [    
    path('logout/', views.LogOut, name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.HomeView.as_view(), name='home'), 
    path('ingredients/', views.IngredientsView.as_view(), name="ingredients"),
    path('ingredients/new', views.NewIngredientView.as_view(), name="add_ingredient"),
    path('ingredients/<slug:pk>/update', views.UpdateIngredientView.as_view(), name="update_ingredient"),    
    path('menu/', views.MenuView.as_view(), name="menu"),
    path('menu/new', views.NewMenuItemView.as_view(), name="add_menu_item"),
    path('menu/<slug:pk>/update', views.UpdateMenuItemView.as_view(), name="update_menu_item"),
    path('reciperequirement/new', views.NewRecipeRequirementView.as_view(), name="add_recipe_requirement"),
    path('reciperequirement/<slug:pk>/update', views.UpdateRecipeRequirementView.as_view(), name="update_recipe_requirement"), 
    path('reciperequirement/<int:menu_item>/new', views.NewRecipeRequirementToMenuItemView.as_view(), name="add_recipe_requirement_to_menu_item"),   
    path('purchases/', views.PurchasesView.as_view(), name="purchases"),
    path('purchases/new', views.NewPurchaseView.as_view(), name="add_purchase"), 
    path('purchases/new_search', views.PurchaseSearchAddView, name="search_add_purchase"), 
    path('reports/', views.ReportView.as_view(), name="reports"),
    path('selection_reports/<date:start_date>/', views.ReportDateSelectionView, name="selection_reports"),   
    path('selection_reports/', views.ReportDateSelectionView, name="selection_reports"),  
           
    
]
