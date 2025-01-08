from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from .models import Friends, BIO, MyProfile, Profile

def home_view(request):
   HTML_STRING = render_to_string('home.html')
   return HttpResponse(HTML_STRING)


def Friends_view(request):
    HTML_STRING1 = render_to_string('friends.html')
    return HttpResponse(HTML_STRING1)
    

def BIO_view(request):
    HTML_STRING2 = render_to_string('bio.html')
    return HttpResponse(HTML_STRING2)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('main')

    else:
         form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def MyProfile_view(request):
    profileinfo = Profile.objects.all()
    profileinfo = {'profileinfo': profileinfo}
    return render(request, "profile.html", profileinfo)

def database_view(request):
        queryset = MyProfile.objects.all()
        queryset = {'queryset':queryset}
        return render(request, "database.html", queryset)

def register_view(request):
     if request.method =='POST':
          form = UserRegisterForm(request.POST) ##Tworzy instancję formularza rejestracji UserRegisterForm na podstawie danych przesłanych w żądaniu POST.
          if form.is_valid():
               username = form.cleaned_data.get('username')
               messages.success(request, f'Account created for {username}!')
               form.save()
               new_user = authenticate(username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
                    )
               login(request, new_user)
               return redirect('main')
     else:
        form = UserRegisterForm()
     return render(request, 'Users/register.html', {'form': form})