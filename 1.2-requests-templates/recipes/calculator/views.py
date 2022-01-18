from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

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
        'pancake': {
            'яйца, шт': 2,
            'молоко, л': 0.2,
            'сахар, кг': 0.075,
            'мука кг': 0.2,
            'растительное масло, л': 0.005,
            'разрыхлитель кг': 0.01
        }
    }
#Функция создает меню с переходом к странице выбранного блюда
def menu(request):
    pages = list(DATA.keys())
    paginat = Paginator(pages, 10)
    page = paginat.get_page(1)
    context = {
        'page': page
    }
    return render(request, 'calculator/pagi.html', context)

#Функция получает имя блюда по адресу запроса при переходе из меню,
#создает новый словарь ингредиентов для выбранного блюда с возможностью изменения
#количества порций через параметр servings.
def recipe(request):
    recipePath = request.path[1:-1]
    serv = request.GET.get('servings', 1)
    newDATA = {}
    newDATA[recipePath] = {}
    for key, value in DATA.get(recipePath).items():
        newDATA[recipePath][key] = value * int(serv)
    context = {
        'recipe': newDATA.get(recipePath),
        'recipePath': recipePath,
    }
    return render(request, 'calculator/index.html', context)
