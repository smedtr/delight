from django.urls import path

from . import views

urlpatterns = [    
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
    path('reports', views.ReportView.as_view(), name="reports"),        
    
]
