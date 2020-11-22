from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth.models import User
from .models import Image,Profile,Comment
from .forms import NewPostForm,NewProfileForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def landing(request):
    posts = Image.get_images()
    current_user = request.user

    suggestions = Profile.objects.all()
    return render(request,"instagram-page/landing.html",{'posts':posts,'user':current_user,'suggestions':suggestions})

def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = current_user
            post.save()
        return redirect('landing')

    else:
        form = NewPostForm()
    return render(request,'new_post.html', {"form": form})  

def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('landing')

    else:
        form = NewProfileForm()
    return render(request,'new_profile.html', {"form": form})                        

# def profile(request):
#     current_user = request.user
#     photos = Image.objects.filter(posted_by=current_user).all()
    
#     return render(request, 'profile.html',{"photos":photos,"profile":profile})        