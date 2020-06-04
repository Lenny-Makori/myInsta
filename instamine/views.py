from django.shortcuts import render, redirect
from .models import Image, Profile
from .forms import ImageForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    image_display = Image.objects.all()

    return render(request, 'mainview/timeline.html', {"image_display":image_display})

def search_results(request):
    if 'userToFollow' in request.GET and request.GET['userToFollow']:
        search_term = request.GET.get("userToFollow")
        # searched_user = Profile.search_by_username(search_term)
        searched_user = User.objects.filter(username__icontains=search_term)
        print(searched_user)
        message = f"{search_term}"

        return render(request, 'mainview/search.html', {"message":message, "searched_user": searched_user})
    else:
        message = "You haven't searched for any term"
        return render(request, 'mainview/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
        if request.method == 'POST':
            commentform = 
    except DoesNotExist:
        raise Http404()
    return render(request,"mainview/image.html", {"image":image})


@login_required(login_url='/accounts/login/')
def profile(request,user_id):
    user_profile = Profile.get_profile(user_id)

    return render(request, 'profile.html', {'user_profile':user_profile})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    current_user_id = current_user.id
    user_profile = Profile.get_profile(user_id)
    print(current_user_id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            user_profile = Profile.get_profile(current_user_id)
            new_profile = Profile.objects.filter(user=current_user_id).update(profile_pic=profile.profile_pic, bio=profile.bio)
            new_profile.save()
            print(new_profile)

        return redirect('profile')
    else:
        form = ProfileForm()

    return render(request, 'profile_edit.html', {"form":form})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('homepage')
    else:
        form = ImageForm()
    return render(request,'new_image.html',{'form':form})

