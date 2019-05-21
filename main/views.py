from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Servers,ServerDetails,Logs


# Create your views here.

@login_required
def homepage(request):
    #return HttpResponse('<h1>hello</h1>')
    if request.user.is_superuser:
        return render(request,"main/home.html",{'serv':Servers.objects.all()})
    else:
        return redirect("main:user_home")


@login_required
def server_details(request,name):
    #return HttpResponse('<h1>hello</h1>')
    obj = get_object_or_404(ServerDetails.objects.all(), hostname=name)
    return render(request, "main/server_details.html", {'serv': obj})

@login_required
def user_homepage(request):
    if request.method == 'POST':
        form = request.POST
        log = Logs(serv_name = form['serv_inp'], user_accessed = request.user.username, reason= form['comment'])
        log.save()
        #obj = get_object_or_404(ServerDetails.objects.all(), hostname=form['serv_inp'])
        return redirect('server_details/'+form['serv_inp'])
    return render(request, "main/user_home.html")

@login_required
def view_logs(request):
    logs = Logs.objects.all()
    return render(request, "main/logs.html", {'logs': logs})


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
