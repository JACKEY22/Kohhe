from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from comment.forms import CommentCreateForm
from comment.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'comment/create.html'

    def get_success_url(self):
        return reverse_lazy('article:detail', kwargs={'pk':self.object.article.pk})


