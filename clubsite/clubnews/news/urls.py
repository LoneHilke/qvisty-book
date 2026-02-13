from django.urls import path
from .views import ArticleListView
from . import views

urlpatterns = [
    path("", ArticleListView.as_view(), name="news_home"),
    path("article/<int:pk>/", views.article_detail, name="article_detail"),
    path("add/", views.add_article, name="add_article"),
    path("edit/<int:pk>/", views.edit_article, name="edit_article"),
    path("delete/<int:pk>/", views.delete_article, name="delete_article"),
]