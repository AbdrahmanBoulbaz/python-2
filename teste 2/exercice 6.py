cookbook = {
  "Sandwich": {
      "ingredients": ["ham", "bread", "cheese", "tomatoes"],
      "meal": "lunch",
      "prep_time": 10
  },
  "Cake": {
      "ingredients": ["flour", "sugar", "eggs"],
      "meal": "dessert",
      "prep_time": 60
  },
  "Salad": {
      "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
      "meal": "lunch",
      "prep_time": 15
  }
}

def print_recipe_names():
  print("Recipe Names:")
  for recipe_name in cookbook:
      print("- " + recipe_name)

def print_recipe_details(recipe_name):
  if recipe_name in cookbook:
      recipe = cookbook[recipe_name]
      print(f"Details of {recipe_name}:")
      print("Ingredients:", ", ".join(recipe["ingredients"]))
      print("Meal:", recipe["meal"])
      print("Preparation Time:", recipe["prep_time"], "minutes")
  else:
      print("Recipe not found in the cookbook.")

def delete_recipe(recipe_name):
  if recipe_name in cookbook:
      del cookbook[recipe_name]
      print(f"{recipe_name} recipe deleted successfully.")
  else:
      print("Recipe not found in the cookbook.")

def add_recipe():
  name = input("Enter recipe name: ")
  ingredients = input("Enter ingredients (separated by comma): ").split(", ")
  meal = input("Enter meal type: ")
  prep_time = int(input("Enter preparation time (in minutes): "))
  cookbook[name] = {
      "ingredients": ingredients,
      "meal": meal,
      "prep_time": prep_time
  }
  print(f"{name} recipe added successfully.")

print_recipe_names()
print()
print_recipe_details("Cake")
print()
delete_recipe("Sandwich")
print()
add_recipe()
print()
print_recipe_names()
