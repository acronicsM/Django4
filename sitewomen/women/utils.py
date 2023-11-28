menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


class DataMixin:
    paginate_by = 3
    title_page = cat_selected = None
    extra_context = dict()

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if 'cat_selected' is not None:
            self.extra_context['cat_selected'] = self.cat_selected

    @staticmethod
    def get_mixin_context(context, **kwargs):
        context['cat_selected'] = None
        context.update(kwargs)

        return context
