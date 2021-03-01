from django.forms import ModelForm

from article.models import Article


class ArticleCreateForm(ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'image', 'shop', 'content']
