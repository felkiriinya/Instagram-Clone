from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth.models import User
from .models import Image,Profile,Comment
from .forms import NewPostForm,NewProfileForm,UpdateUserProfileForm,UpdateUserForm
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
# 
# 
@login_required(login_url='/accounts/login')
def profile(request, username):
    # images = request.user.profile.posts.all()
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm
        prof_form = UpdateUserProfileForm
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        # 'images': images,   

    }
    return render(request, 'profile.html', params)
@login_required(login_url='/accounts/login')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.posts.all()
    users = User.objects.get(username=username)
    followers = len(Follow.objects.followers(users))
    following = len(Follow.objects.following(users))
    people_following = Follow.objects.following(request.user)
    id = request.user.id
    follow_status = None
    params = {
        'user_prof': user_prof,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status,
        'people_following':people_following
    }
    return render(request, 'user_profile.html', params)       