recipes = {}
with open('recipes.txt', 'r', encoding='utf8') as f_recipes:
    for dish in f_recipes:
        amount = int(f_recipes.readline())
        ing_list = []
        for _ in range(0, amount):
            ingredient = f_recipes.readline()[:-1].split(' | ')
            ing_list.append({'ingredient_name': ingredient[0], 'quantity': float(ingredient[1]), 'measure': ingredient[2]})
        recipes[dish[:-1]] = ing_list
        f_recipes.readline()

print(recipes)
