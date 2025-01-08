
from django.http import HttpResponse
from django.shortcuts import render
from UserProfile.models import Profile

def home_view(request):
   profileinfo = Profile.objects.all()
   profileinfo = {'profileinfo': profileinfo}
   return render(request, "main\index.html", profileinfo)

#request - httprequest All attributes should be considered read-only, unless stated otherwise.
#"profileinfo" - stworzenie słownika z kluczem 'profileinfo' o wartości profileinfo przydatne 
# przy modyfikowaniu struktury danych przed przekazaniem do html