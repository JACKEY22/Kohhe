from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from proFile.decorators import profile_ownership_required
from proFile.forms import ProfileCreateForm
from proFile.models import Profile

permission = [login_required(login_url='account:login'),profile_ownership_required]

@method_decorator(login_required(login_url='account:login'), 'get')
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('account:detail', kwargs={'pk':self.object.user.pk})

@method_decorator(permission, 'get')
@method_decorator(permission, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/update.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('account:detail', kwargs={'pk':self.object.user.pk})


