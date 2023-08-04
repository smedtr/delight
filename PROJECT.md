# Django Delights Inventory Tracker

# Overview
In this project, you will bring together what you have learned in the previous lessons and build a project off of Codecademy. You will need to create your own files, write your own code, and publish the final product. We'll provide you with high-level tasks to guide your project to completion, but you will be responsible for deciding how to implement them in your code. There are many possible ways to correctly fulfill all of these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter a problem that you cannot easily solve.

## Project Title
Django Delights Inventory Tracker

## Hours to Complete
10

## Short Overview
Counting and aggregating data is a typical use case for Python, and Python has some powerful ways to process and generate visualizations for data. Django allows us to bring that power of Python data processing to the web, and easily store, format, and display that data using Django views. This project has you create an app to help a restaurant owner keep track of his inventory and sales.

## Long Overview
For this project, you will build an application for a restaurant owner to keep track of how much food he has throughout the day. The owner starts the day with:
- An inventory of different `Ingredient`s, their available quantity, and their prices per unit
- A list of the restaurant's `MenuItem`s, and the price set for each entry
- A list of the ingredients that each menu item requires (`RecipeRequirement`s)
- A log of all `Purchase`s made at the restaurant

Your user (the restaurant owner) should be able to enter in new recipes along with their recipe requirements, and how much that menu item costs. They should also be able to add to the inventory a name of an ingredient, its price per unit, and how much of that item is available.

Lastly, they should be able to enter in a customer purchase of a menu item. When a customer purchases an item off the menu, the inventory should be modified to accommodate what happened, as well as recording the time that the purchase was made.

Your ingredients, recipes, and purchase data should be stored in a database, and should be rendered back to the Django views. Your Django backend should supply endpoints to create new recipes via a form submission, submit customer purchases from a different form, and get information about the total cost of inventory, the total revenue for the day, the different purchases that were made, and how much inventory is required to restock (as an initial example) to render them into a Django view. This view can be tabular or as a chart; get creative!

## Project Objectives

- Build an inventory and sales application using Django
- Develop locally on your machine
- Version control your application with Git and host the repository on GitHub
- Use the command line to manage your application locally and test out queries
- Users can log in and log out, and must be logged in to see the views
- Users can create items for the menu
- Users can add ingredients to the restaurant's inventory and update their quantities
- Users can add the different recipe requirements for each menu item
- Users can record purchases of menu items (only the ones that are able to be created with what's in the inventory!)
- Users can view the current inventory, menu items, their ingredients, and a log of all purchases made

## Prerequisites
- HTML
- CSS
- Python
- Django
- Git
- Command Line

# Setup
## Going off-platform
You will be doing this project outside of the Codecademy platform, on your own computer. 

For this particular project, you will be using your own text editor (we suggest [VS Code](https://code.visualstudio.com/download)) and Git version control. If you need help setting up your text editor, read our [article about setting up a text editor for web development](https://www.codecademy.com/articles/visual-studio-code). If you need a refresher on how to work with Git for version control, [review the Git lesson](https://www.codecademy.com/learn/learn-git) or look at this [cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf).

# Tasks

## Plan your project
Visualize your end result. What is it built with? What can it do? Make sure that it satisfies all of the project objectives. The following tasks will help you identify natural break points.

Make a timeline for yourself and avoid the temptation to build things that aren't required. Setting firm boundaries and deadlines will keep you on track and prevent [scope creep](https://en.wikipedia.org/wiki/Scope_creep).


## Wireframe your application
Using pencil and paper, or a wireframing software of your choice, draft what you'd like your application's views to look like. 

HINT
Think about what the main components of the site will be and how you would like to see them arranged on the page. You should also think about the user flow and design all of those states and transitions as well. Don’t forget about error states!

You should also think about:
- The application’s color palette
- How to break up your design into components
- How your application will look at different screen sizes


## Setup your workspace

To get started, create a Python virtual environment. This will be used to manage all of your dependencies for the project.

To create and activate your virtual environment, run the following commands in your shell:

```bash
python3 -m venv venv
source venv/bin/activate # remember to run this command any time you open the project to work on it
```

## Install Django in your virtual environment

Run:

```bash
pip install django
```

## Create the skeleton for your Django app

Use the `django-admin` CLI to initialize your project and use the `manage.py` tool inside to create our inventory app.

Run:
```bash
django-admin startproject djangodelights
cd djangodelights
python manage.py startapp inventory
```

## Version control
Set up the folder you created previously to be a Git repository. Push the initial files to a repository on GitHub. You should be consistently committing your changes throughout the project. Make sure to have meaningful commit messages.

HINT
To initialize your Git repository, you can run the below code in your terminal, where `application` is the name of your project folder.

```git init```

If you want a refresher on the syntax, look back at the [Git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf).

## Understand the database models

For this project, we'll have four models. Add definitions for each of these in `models.py`, so we can get started on creating some sample data for our inventory app that we can play around with.

### `Ingredient`
This model represents an ingredient that the restaurant has in its inventory.

An ingredient should have the following fields (at least):
- **`name`**: the name of the ingredient (i.e. `flour`)
- **`quantity`**: the quantity of the ingredient available in the inventory (i.e. `4.5`)
- **`unit`**: the unit used for the ingredient (i.e. `tbsp` or `lbs`)
- **`unit_price`**: the price per unit of the ingredient (i.e. `0.05`, for a `tbsp` of `flour`)

### `MenuItem`
This model represents an item on the restaurant's menu.

A menu item should have the following fields (at least):
- **`title`**: the title of the item on the menu (i.e. `Django Juice`)
- **`price`**: the price of the item (i.e. `3.49` for a glass)

### `RecipeRequirement`
This model represents a single ingredient and how much of it is required for an item off the menu.

A recipe requirement should have the following fields (at least):
- **`menu_item`**: a reference to an item on the menu (i.e. a foreign key to the `MenuItem` model)
- **`ingredient`**: a reference to a required ingredient for the associated menu item (i.e. a foreign key to the `Ingredient` model)
- **`quantity`**: the amount of the associated ingredient that is required to create the menu item (i.e. `1.5` ounces of `sugar` to create `Django Djaffa Cake`)


### `Purchase`
This model represents a customer purchase of an item off the menu.

A purchase should have the following fields (at least):
- **`menu_item`**: a reference to an item on the menu (i.e. a foreign key to the `MenuItem` model)
- **`timestamp`**: a timestamp indicating the time that the purchase was recorded (i.e. a `DateTimeField`)

### `Migrating the tables into the database`
Run:
```bash
python manage.py makemigrations
python manage.py migrate
```

### `Creating a superuser and adding the tables to the admin interface`
Run:
```bash
python manage.py createsuperuser
```
Created a superuser : super

## Populating some sample data

### Added fixtures 
Dump of the data : 
```bash
python manage.py dumpdata inventory > inventory.json
```
Loading of the data. If this is an empty db:

```bash
python manage.py loaddata inventory.json
```

### Via a command shell adding data
```bash
python manage.py shell
``` 
```bash
from inventory.models import MenuItem, Ingredient, RecipeRequirement

jaffa_cake = MenuItem(title="Djaffa Cake",price=5.00)
jaffa_cake.save()
MenuItem.objects.all().values()

confituur = Ingredient(name="Sinaasappel confituur",quantity=250.00,unit="g",unit_price=0.00089)
confituur.save()
ei = Ingredient(name="Ei",quantity=12.00,unit="stk",unit_price=0.25)
ei.save()
riet_suiker = Ingredient(name="Rietsuiker",quantity=1000.00,unit="g",unit_price=0.00089)
riet_suiker.save()
bloem = Ingredient(name="Bloem",quantity=1000.00,unit="g",unit_price=0.0425)
bloem.save()
chocolade = Ingredient(name="Melkchocolade",quantity=250.00,unit="g",unit_price=0.00675)
chocolade.save()
ei = Ingredient.objects.filter(name="Ei").first()
bloem = Ingredient.objects.filter(name="Bloem").first()
jaffa_cake_recipe = RecipeRequirement(menu_item=jaffa_cake,ingredient=confituur,quantity=100.0)
jaffa_cake_recipe.save()
jaffa_cake_recipe = RecipeRequirement(menu_item=jaffa_cake,ingredient=ei,quantity=1.0)
jaffa_cake_recipe.save()
jaffa_cake_recipe = RecipeRequirement(menu_item=jaffa_cake,ingredient=riet_suiker,quantity=150.0)
jaffa_cake_recipe.save()
jaffa_cake_recipe = RecipeRequirement(menu_item=jaffa_cake,ingredient=bloem,quantity=100.0)
jaffa_cake_recipe.save()
jaffa_cake_recipe = RecipeRequirement(menu_item=jaffa_cake,ingredient=chocolade,quantity=600.0)
jaffa_cake_recipe.save()

```
### An example
Here are the ingredients for **Django Djaffa Cake**:

- 100 grams of orange jelly
- 1 large egg
- 1.5 ounces cane sugar
- 1 ounces flour
- 6 ounces milk chocolate

First, we'd create the item on our menu by creating an entry in the menu item's table:

**`MenuItem` Model**

| id  | Title              | Price |
| --- | ------------------ | ----- |
| 1   | Django Djaffa Cake | 8.25  |

In our ingredients table, we would want to ensure that all of those ingredients are present, at least.

**`Ingredient` Model**

| id  | Name           | Quantity | Unit   | Unit Price |
| --- | -------------- | -------- | ------ | ---------- |
| 1   | orange jelly   | 300      | grams  | 0.03       |
| 2   | eggs           | 12       | eggs   | 0.30       |
| 3   | cane sugar     | 50.5     | ounces | 0.65       |
| 4   | flour          | 24.5     | ounces | 0.80       |
| 5   | milk chocolate | 20.8     | ounces | 1.40       |
| 6   | feta cheese    | 3.5      | lbs    | 4.00       |

In our recipe requirements table, we would have have 5 entries:

**`RecipeRequirement` Model**

| id  | Menu Item | Ingredient | Quantity |
| --- | --------- | ---------- | -------- |
| 1   | 1         | 1          | 100.0    |
| 2   | 1         | 2          | 1.0      |
| 3   | 1         | 3          | 1.5      |
| 4   | 1         | 4          | 1.0      |
| 5   | 1         | 5          | 6.0      |

Lastly, when someone wishes to purchase a **Django Djaffa Cake**, we would allow them to select that item off the menu, add a timestamp for when they purchased it, and (after making sure we have enough of the required ingredients in our inventory), we would subtract the required quantities from the inventory and record their purchase.

**`Purchase` Model**

| id  | Menu Item | Timestamp                |
| --- | --------- | ------------------------ |
| 1   | 1         | March 4, 2021, 4:18 p.m. |

### Generating and querying our sample data

After we're done creating our models, we can install the inventory app in the `djangodelights/settings.py`.

Once this is done, generate and run the database migrations migrations for the inventory app.

```bash
python manage.py makemigrations
python manage.py migrate
```

Then, you can use either the Django shell or the Django admin UI to create your sample data as described above. 

Remember, to use the admin site, we'll have to create a superuser first with:

```bash
python manage.py createsuperuser
```

We'll also need to edit `admin.py` to register each of our models with the admin site.

Generating this data early on in your development process will give you the opportunity to try out some sample queries and views with data behind them as soon as possible.

To test out the queries that you think you'll need in your code, you can use the Django shell with `python manage.py shell`.

## Write your queries
For this inventory app to be useful for our restaurant owner, we would want our app to be able to answer the following questions:

- What is currently in the restaurant's inventory?
- What purchases have been made?
- What does the restaurant's menu look like? What ingredients (and how many of each) are required for each item on the menu? What's the price of each item?
- What is the total `revenue` for the restaurant over all recorded purchases?
- What is the total `cost` to the restaurant over all purchases made (sum of cost of all ingredients used).
- How much `profit` (`revenue` - `cost`) does the restaurant make?

The majority of the above queries can be made quite easily using Django's generics. For the last one, you'll need to do some computation across multiple models. It will be easier to do so using some custom values that we can supply to our template with the `get_context_data` function in a `TemplateView`. Try creating the queries and testing your logic in the Django shell before you execute it in a template.

### Looking for the ingredients of a MenuItem
```bash
python manage.py shell
from inventory.models import MenuItem, Ingredient, RecipeRequirement, Purchase
jaffa_cake = MenuItem.objects.filter(title="Djaffa Cake").first()
jaffa_cake.reciperequirement_set.all()
```
### Looking if there is sufficient remaining if the ingredient
Check how much eggs we would need in the Djaffa Cake recepie
```bash
python manage.py shell
from inventory.models import MenuItem, Ingredient, RecipeRequirement, Purchase
jaffa_cake = MenuItem.objects.filter(title="Djaffa Cake").first()
ei_ingredient = Ingredient.objects.filter(name="Ei").first()
ei_requirement = RecipeRequirement.objects.filter(menu_item=jaffa_cake, ingredient=ei_ingredient).first()
print(ei_requirement)
print(ei_ingredient)
print(ei_requirement.enough())
print(ei_requirement.cost())
```
### Return the profit of a MenuItem
Return the profit of individual MenuItem
Calculate the cost of an ingredient in a recipe.
```bash
python manage.py shell
from inventory.models import MenuItem, Ingredient, RecipeRequirement, Purchase
jaffa_cake = MenuItem.objects.filter(title="Djaffa Cake").first()
ei_ingredient = Ingredient.objects.filter(name="Ei").first()
ei_requirement = RecipeRequirement.objects.filter(menu_item=jaffa_cake, ingredient=ei_ingredient).first()
print(ei_requirement.cost())
```
```bash
python manage.py shell
from inventory.models import MenuItem, Ingredient, RecipeRequirement, Purchase
jaffa_cake = MenuItem.objects.filter(title="Djaffa Cake").first()
jaffa_cake_ingredients = RecipeRequirement.objects.filter(menu_item=jaffa_cake)
print(jaffa_cake_ingredients)
print(jaffa_cake.available())
print(jaffa_cake.cost())
print(jaffa_cake.profit())

```
## Table layouts 
As a lot of this is displayed via tables could be OK to review this. See perhaps : https://dev.to/dcodeyt/creating-beautiful-html-tables-with-css-428l


## Creating views and templates
To enable a full suite of CRUD functionality for our inventory app, we'll require one templates for each of the following:

- a base template for all the other pages to inherit from, with common styling and a navbar linking to the other pages
- a home page
- a page to view all ingredients in the inventory
- a page to view the menu
- a page to view the purchases made at the restaurant
- a page to view the profit and revenue report
- a page to add an item to the menu
- a page to add an ingredient to the inventory
- a page to add the recipe requirements for a menu item
- a page to record a new purchase of a menu item
- a page to update the inventory for an existing ingredient


Create templates appropriately inside `inventory/templates/inventory`, taking care to use all of Django's generics functionality (`ListView`, `CreateView`, `UpdateView`, `TemplateView`) to make this easier for you.

As you finish each template, add the corresponding view to `views.py` and create the `path` entry in `inventory/urls.py`. This will allow you to test the functionality for each model as you proceed through the implementation.

After the above are implemented, feel free to implement any more functionality you think would be useful for our restaurant owner as an added exercise!

## Authentication
Create a log in and log out page for our inventory application.

All of the views that are mentioned above should require the user to be authenticated first. You'll have to create another template for your login page, and leverage the `LoginRequiredMixin` in all of the views above (except the login and logout views).

To test out your authentication functionality, you can use the super-user you created when we used the Django admin UI earlier in the project. You can also use that UI to create more users!

# Extra Credit
- Be able to upload / render images alongside recipes or ingredients.
- Be able to Deploy the app to PythonAnywhere 

# Resources
## Debugging Tips
Feeling stuck? Try the following:
*Google your question:* often times, someone has had the same question as you! Check out websites like StackOverflow and Quora to see how other folks have found solutions. 
*Read the documentation:* make sure to carefully read through the documentation for any languages and libraries that you are using. Oftentimes they'll have examples of what you're looking for!
*Rubber ducking:* try to explain a problem to a friend or co-worker. Oftentimes you'll figure out the solution as you're trying to explain it. And if not, getting another pair of eyes on your code can be helpful. 

## Example Code
Want to see an example of how someone else has completed this project? Click this [link](https://git.khayyam.me/codecademy-content/bwa-django-final-project/archive/main.zip) to download a zip file containing one example solution to this project. Remember: your project doesn't have to look anything like this! It should be unique to your vision.

# Sharing
Great work! Visit [our forums](https://discuss.codecademy.com/) to compare your project to our sample solution code. After you host your own solution on GitHub, be sure to share it with other learners and see how other learners have built their own projects!

Your solution might look different from ours, and that’s okay! There are multiple ways to solve these projects, and you’ll learn more by seeing others’ code.

As you continue to learn, make sure to keep adding projects to your portfolio (especially Portfolio Projects!).
