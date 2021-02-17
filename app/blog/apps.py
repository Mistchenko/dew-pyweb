from django.apps import AppConfig


class BlogConfig(AppConfig):
    """ Настройка приложения

    Пример использования:
    ```
    from django.apps import apps
    apps.get_app_config('blog').verbose_name
    ```

    Документация: https://docs.djangoproject.com/en/3.1/ref/applications/
    """
    name = 'blog'
    verbose_name = 'Статьи для блога'
