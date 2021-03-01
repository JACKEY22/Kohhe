from django.forms import ModelForm
from django import forms
from comment.models import Comment


class CommentCreateForm(ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable;',
                                                                        'style':'max-height: 4rem;',
                                                                       'placeholder':'댓글을 작성해주세요.'}))

    class Meta:
        model = Comment
        fields = ['content']