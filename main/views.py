from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Servers,ServerDetails


# Create your views here.

@login_required
def homepage(request):
    #return HttpResponse('<h1>hello</h1>')
    return render(request,"main/home.html",{'serv':Servers.objects.all()})

@login_required
def server_details(request,name):
    #return HttpResponse('<h1>hello</h1>')
    obj = get_object_or_404(ServerDetails.objects.all(), hostname=name)
    return render(request, "main/server_details.html", {'serv': obj})


'''
def user_login(request):
    if request=='POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            #user =
            #login(user)
    form = AuthenticationForm()
    return render(request, "main/user_login.html", {'form': form})
'''