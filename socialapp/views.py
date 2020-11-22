from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth.models import User
from .forms import NewPostForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def landing(request):
    return render(request,"instagram-page/landing.html")

def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = current_user
            post.save()
        return redirect('landing')

    else:
        form = NewPostForm()
    return render(request,'new_post.html', {"form": form})                    