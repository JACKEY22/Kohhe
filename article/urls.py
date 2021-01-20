from django.urls import path
from django.views.generic import TemplateView

from article.views import ArticleCreateView, ArticleListView

app_name = 'article'
urlpatterns = [

    path('list/', ArticleListView.as_view(), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),

]