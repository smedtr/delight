from django import forms
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"

class RecipeRequirementMenuItemForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('ingredient','quantity')

class PurchaseMultiMenuItemForm(forms.Form):
    menu_items_choices = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset = MenuItem.objects.all(),
        initial = 0
        )

