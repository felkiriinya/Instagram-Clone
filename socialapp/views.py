from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
# Create your views here.
@login_required(login_url='/accounts/login/')
def landing(request):
    return render(request,"instagram-page/landing.html")