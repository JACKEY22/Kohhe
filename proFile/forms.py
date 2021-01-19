from django.forms import ModelForm

from proFile.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']
