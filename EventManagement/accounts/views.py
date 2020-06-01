from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from accounts.forms import UserExtraInfoForm, UserCreateForm
from accounts.models import UserExtraInfo
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


User = get_user_model()

# Create your views here.

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"


class CreateUserExtraView(LoginRequiredMixin, CreateView):
    form_class = UserExtraInfoForm
    model = UserExtraInfo

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdateUserExtraView(LoginRequiredMixin, UpdateView):
    model = UserExtraInfo
    form_class = UserExtraInfoForm


class UserDetailView(DetailView):
    model = User
    context_object_name = 'event_organiser'
    template_name = 'accounts/user_detail.html'




# function view for CreateUserExtraView:
# @login_required
# def create_user_extra_view(request):  
#     if request.method == 'POST': 
#         form = UserExtraInfoForm(request.POST, request.FILES) 
#         if form.is_valid(): 
#             user_info = form.save(commit=False)
#             user_info.user = User.objects.get(pk=request.user.pk)
#             user_info.save()
#             return HttpResponseRedirect(reverse_lazy('accounts:user_detail', kwargs={"pk":request.user.pk}))
#     else: 
#         form = UserExtraInfoForm()
#     return render(request, 'accounts/userextrainfo_form.html', {'form':form}) 