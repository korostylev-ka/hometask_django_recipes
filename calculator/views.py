from django.shortcuts import render
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def home_page(request):
    template_name = 'calculator/home.html'
    dishes_links = {}

    for dish in DATA:
        dishes_links[dish] = f'{reverse('home')}{dish}'
    context = {
        'dishes_links': dishes_links
    }
    return render(request, template_name, context=context)

def get_ingredients(request, food_name):
    home_page = reverse('home')
    param_name = 'servings'
    servings = request.GET.get(param_name)
    values = int(servings) if servings != None else 1
    template_name = 'calculator/index.html'
    recipe_values = {}
    wrong_dish_name = 'wrong dish name'
    ingredients = DATA.get(food_name, wrong_dish_name)
    if ingredients == wrong_dish_name:
        context = {
            'food_name': food_name,
            'home': home_page
        }
        return render(request, 'calculator/404.html', context)
    for items in ingredients:
        recipe_values[items] = ingredients[items] * values
    context = {
        'recipe': recipe_values,
        'title': food_name,
        'home': home_page
    }
    return render(request, template_name, context=context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
