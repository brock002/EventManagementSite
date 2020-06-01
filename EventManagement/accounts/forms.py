from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserExtraInfo
from django import forms

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()
        
class UserExtraInfoForm(forms.ModelForm):

    class Meta:
        model = UserExtraInfo
        exclude = ['user',]
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }
        labels = {
            'full_name': ('Your Full Name'),
            'profile_pic': ('Your Photo'),
        }