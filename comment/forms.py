from django.forms import ModelForm
from django import forms
from comment.models import Comment


class CommentCreateForm(ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable',
                                                           'style':'height: auto;'}))

    class Meta:
        model = Comment
        fields = ['content']