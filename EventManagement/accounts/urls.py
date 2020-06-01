from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('details/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    path('add/info', views.CreateUserExtraView.as_view(), name='create_user_extra'),
    path('edit/info/<int:pk>', views.UpdateUserExtraView.as_view(), name='update_user_extra'),
]