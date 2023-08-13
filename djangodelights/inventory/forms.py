import datetime
from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.forms import ValidationError
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

class ReportDateSelectionForm(forms.Form):
    startdate = forms.DateField(initial=datetime.date.today)
    enddate = forms.DateField(initial=datetime.date.today)  

    def clean(self) :
        cleaned_data = super().clean()
        start_date = cleaned_data['startdate']
        end_date = cleaned_data['enddate']
        if end_date < start_date :
            raise ValidationError(_('Invalid date - Startdate must be before the Enddate'))
        return cleaned_data 

    def clean_startdate(self):
        data = self.cleaned_data['startdate']

        # Check if a date is not in the past.
        if data < datetime.date.today() + datetime.timedelta(weeks=-4):
            raise ValidationError(_('Invalid date - Startdate should not be older then 4 weeks'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - Startdate should not be more then 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data
    
    def clean_enddate(self):
        data = self.cleaned_data['enddate']

        # Check if a date is not in the past.
        if data < datetime.date.today() + datetime.timedelta(weeks=-4):
            raise ValidationError(_('Invalid date - Enddate should not be older then 4 weeks'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - Startdate should not be more then 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

