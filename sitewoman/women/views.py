from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


class MyClass:
    def __init__(self, a, b):
        self.a, self.b = a, b


def index(request: HttpRequest):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'float': 28.56,
        'lst': [1, 2, 'abc', True],
        'set': {1, 2, 3, 2, 5},
        'dict': {'key1': 'value1', 'key2': 'value2'},
        'obj': MyClass(10, 20)
    }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def categories(request: HttpRequest, cat_id: int):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')


def categories_by_slug(request: HttpRequest, cat_slug: str):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')


def archive(request: HttpRequest, year: int):
    if year > 2023:
        uri = reverse('cats', args=('music', ))
        return redirect(uri)

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
