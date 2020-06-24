from django.db import models
from django.contrib import auth
from django.contrib.auth import get_user_model

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.first_name + self.last_name


class UserExtraInfo(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=300)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics/')

    def __str__(self):
        return self.user.username + "'s Extra Info"
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('accounts:user_detail', kwargs={'pk': self.user.pk})
