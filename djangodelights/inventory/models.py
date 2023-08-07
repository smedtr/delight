from django.db import models

# Create your models here.

class Ingredient(models.Model):
    ##
    # An ingredient should have the following fields (at least):
    #name: the name of the ingredient (i.e. flour)
    #quantity: the quantity of the ingredient available in the inventory (i.e. 4.5)
    #unit: the unit used for the ingredient (i.e. tbsp or lbs)
    #unit_price: the price per unit of the ingredient (i.e. 0.05, for a tbsp of flour)
    ##
    
    class UnitType(models.TextChoices):
        GRAM = "g"
        CENTILITER = "cl"
        KOFFIELEPEL = "kl"
        EETLEPEL = "el"
        STUK = "stk"

    name = models.CharField(max_length=200)
    quantity = models.FloatField(default=0.00, verbose_name="quantity in stock")    
    unit = models.CharField(blank=True, choices=UnitType.choices, max_length=15)    
    unit_price = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/ingredients"

    def __str__(self):
        return f"""
        name={self.name};
        qty_in_stock={self.quantity};
        unit={self.unit};
        unit_price={self.unit_price}
        """
    
class MenuItem(models.Model):
    ##
    #A menu item should have the following fields (at least):
    #- **`title`**: the title of the item on the menu (i.e. `Django Juice`)
    #- **`price`**: the price of the item (i.e. `3.49` for a glass)
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return f"""
        title={self.title};
        price={self.price}
        """
    
    def get_absolute_url(self):
        return "/menu"
    
    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())

    def cost(self):   
        ## Voor de Jaffa Cake
        #Jaffa Cake
        #Chocolade 150g 0.00675 = 1.0125
        #Bloem 100g 0.00425 = 0.425
        #Rietsuiker 150g 0.00089 = 0.1335
        #Ei 1st 0.25 = 0.25
        #Confituur 100g 0.00089 = 0.089
        # Total Cost 1.91
        # Total Profit = 5.00 - 1,91 = 3.09
        ##
        #total_cost = all(X.cost() for X in self.reciperequirement_set.all())
        # all geeft een true of false of mee dus waarde 1 dit geeft dan dat profit 4 is 5.0 - 1 = 4.0     
        total_cost = 0
        for X in self.reciperequirement_set.all() :
            total_cost = total_cost + X.cost()  
        return total_cost
    
    def profit(self):                
        total_profit = self.price - self.cost()
        return total_profit
    
    
    
class RecipeRequirement(models.Model):
    ## `RecipeRequirement`
    #This model represents a single ingredient and how much of it is required for an item off the menu.
    #A recipe requirement should have the following fields (at least):
    #- **`menu_item`**: a reference to an item on the menu (i.e. a foreign key to the `MenuItem` model)
    #- **`ingredient`**: a reference to a required ingredient for the associated menu item (i.e. a foreign key to the `Ingredient` model)
    #- **`quantity`**: the amount of the associated ingredient that is required to create the menu item (i.e. `1.5` ounces of `sugar` to create `Django Djaffa Cake`)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.00)

    def __str__(self):
        return f"""
        menu_item=[{self.menu_item.__str__()}];
        ingredient={self.ingredient.name};
        qty={self.quantity}
        """
    
    def get_absolute_url(self):
        return "/menu"
            
    def enough(self):
        return self.quantity <= self.ingredient.quantity
            
    def cost(self):        
        return self.quantity * self.ingredient.unit_price

class Purchase(models.Model):
    ## `Purchase`
    #This model represents a customer purchase of an item off the menu.
    #A purchase should have the following fields (at least):
    #- **`menu_item`**: a reference to an item on the menu (i.e. a foreign key to the `MenuItem` model)
    #- **`timestamp`**: a timestamp indicating the time that the purchase was recorded (i.e. a `DateTimeField`)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"""
        menu_item=[{self.menu_item.__str__()}];
        time={self.timestamp}
        """
    