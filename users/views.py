from django.shortcuts import render

from .forms import CustomUserCreationForm

class SignupPageView(CreateView): 
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('login') 
    template_name = 'signup.html'

