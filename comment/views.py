from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from article.models import Article
from comment.decorators import comment_ownership_required
from comment.forms import CommentCreateForm
from comment.models import Comment

permission = [login_required, comment_ownership_required]

@method_decorator(login_required(login_url='account:login'), 'get')
@method_decorator(login_required(login_url='account:login'), 'post')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'comment/create.html'

    def form_valid(self, form):
        temp_form = form.save(commit=False)
        temp_form.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_form.writer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article:detail', kwargs={'pk':self.object.article.pk})

@method_decorator(permission, 'get')
@method_decorator(permission, 'post')
class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse_lazy('article:detail', kwargs={'pk':self.object.article.pk})



