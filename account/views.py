from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from account.decorators import login_ownership_required
from account.forms import AccountUpdateFrom
from article.models import Article
from subscription.models import Subscription

permission = [login_required, login_ownership_required]

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    template_name = 'account/detail.html'
    context_object_name = 'target_user'
    #paginate_by = 10

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        user = self.request.user
        target_user = self.object
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, target_user=target_user)
        else:
            subscription = None
        return super(AccountDetailView, self).get_context_data(object_list=object_list,
                                                               subscription=subscription,
                                                               **kwargs)

@method_decorator(permission, 'get')
@method_decorator(permission, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateFrom
    template_name = 'account/update.html'

    def get_success_url(self):
        return reverse_lazy('account:detail', kwargs={'pk':self.object.pk})

    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()

@method_decorator(permission, 'get')
@method_decorator(permission, 'post')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('account:login')
    template_name = 'account/delete.html'


