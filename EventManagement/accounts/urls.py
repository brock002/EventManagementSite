from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html', success_url=reverse_lazy('accounts:password_change_done')), name='password_change'),
    path('change-password-done/',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/change_password_done.html'), name='password_change_done'),
    path('details/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    path('add/info', views.CreateUserExtraView.as_view(), name='create_user_extra'),
    path('edit/info/<int:pk>', views.UpdateUserExtraView.as_view(), name='update_user_extra'),
]