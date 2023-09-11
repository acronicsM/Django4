from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.shortcuts import render

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


class MyClass:
    def __init__(self, a, b):
        self.a, self.b = a, b


data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография', 'is_published': True},
]


def index(request: HttpRequest):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'float': 28.56,
        'lst': [1, 2, 'abc', True],
        'set': {1, 2, 3, 2, 5},
        'dict': {'key1': 'value1', 'key2': 'value2'},
        'obj': MyClass(10, 20),
        'posts': data_db,
    }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def show_post(request: HttpRequest, post_id: int):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def addpage(request: HttpRequest):
    return HttpResponse(f'Добавление статьи')


def contact(request: HttpRequest):
    return HttpResponse(f'Контакты')


def login(request: HttpRequest):
    return HttpResponse(f'Авторизация')


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
