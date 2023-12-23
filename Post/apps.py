from django.apps import AppConfig
from watson import search


class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Post'

    def ready(self):
        post = self.get_model("Post")
        search.register(post, fields=["category__name", "author__name", "body", "title"])

