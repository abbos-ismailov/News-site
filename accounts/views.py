from django.shortcuts import render
from .forms import RegistrationForm, UserUpdateForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
) 
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
# Create your views here.

class RegistrationView(CreateView): ### Bu tayyor bolgandan keyin urlga turilimiz
    template_name = 'registration/register.html'
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('home') 

class MyProfileView(LoginRequiredMixin, UpdateView):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        context = {
            'user': user
        }
        return render(request, "user/my_profile.html", context)


class MyProfileUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse_lazy("my_profile")

    template_name = "user/user_update_view.html"
    
    def test_func(self): #### Nimaga buni ichiga kirmadi
        obj = self.get_object()
        print(obj, "Bu obj <-------------------------------")
        return obj.user == self.request.user or self.request.user.is_superuser