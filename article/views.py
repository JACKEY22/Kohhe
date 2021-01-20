

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from article.forms import ArticleCreateForm
from article.models import Article

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'article/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('account:detail', kwargs={'pk':self.object.writer.pk})

class ArticleListView(ListView):
    model = Article
    template_name = 'article/list.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.all()