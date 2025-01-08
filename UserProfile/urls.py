from django.urls import path

from . import views
from .views import home_view

app_name = 'UserProfile'
urlpatterns = [
    path('', home_view),
    path('friends/', views.Friends_view, name='friends'),
    path('bio/', views.BIO_view, name='bio'),
    path('profile/', views.MyProfile_view, name='userprofile'),
    path('database/', views.database_view, name='database'),
    path('register/', views.register_view, name='registration'),
    path('login/', views.login_view, name='login')
]