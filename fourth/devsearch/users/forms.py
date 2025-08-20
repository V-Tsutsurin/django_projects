from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': "Name"
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'bio', 'short_info', 'profile_image', 'social_github',
                  'social_youtube', 'social_website']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'input'})