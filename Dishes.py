recipes = {}
with open('recipes.txt', 'r', encoding='utf8') as f_recipes:
    for dish in f_recipes:
        amount = int(f_recipes.readline())
        ing_list = []
        for _ in range(0, amount):
            ingredient = f_recipes.readline().replace('\n', '').split(' | ')
            ing_list.append({'ingredient_name': ingredient[0], 'quantity': float(ingredient[1]), 'measure': ingredient[2]})
        recipes[dish[:-1]] = ing_list
        f_recipes.readline()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in recipes.keys():
            for ing in recipes[dish]:
                ing_name, ing_quantity, ing_measure = ing['ingredient_name'], ing['quantity'], ing['measure']
                if ing_name in shop_list.keys():
                    shop_list[ing_name]['quantity'] += ing_quantity * person_count
                else:
                    shop_list[ing_name] = {'measure': ing_measure, 'quantity': ing_quantity * person_count}
        else:
            return 'Рецепт как минимум одного блюда не найден'
    return shop_list


# print(recipes)
print(get_shop_list_by_dishes(['Утка по-пекински', 'Чай'], 6))
