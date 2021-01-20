
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from proFile.decorators import profile_ownership_required
from proFile.forms import ProfileCreateForm
from proFile.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    success_url = reverse_lazy('account:hello_world')
    template_name = 'profile/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreateForm
    success_url = reverse_lazy('account:hello_world')
    template_name = 'profile/update.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

