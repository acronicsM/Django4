from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.shortcuts import render


def index(request: HttpRequest):
    return HttpResponse('Страница приложения women')


def categories(request: HttpRequest, cat_id: int):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')


def categories_by_slug(request: HttpRequest, cat_slug: str):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')


def archive(request: HttpRequest, year: int):
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')