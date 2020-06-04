from django.shortcuts import render, redirect
from .models import Image, Profile
from .forms import ImageForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    image_display = Image.objects.all()

    return render(request, 'mainview/timeline.html', {"image_display":image_display})

@login_required(login_url='/accounts/login/')
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
    except DoesNotExist:
        raise Http404()
    return render(request,"mainview/image.html", {"image":image})


@login_required(login_url='/accounts/login/')
def profile(request,user_id):
    print(user_id)
    user_profile = Profile.get_profile(user_id)

    return render(request, 'profile.html', {'user_profile':user_profile})

@login_required(login_url='/accounts/login/')
# @transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            current_user = user_form.save()
            # profile_form.save()
            profile = profile_form.save(commit=False)
            profile.user = current_user.id
            profile.save()
        return redirect('profileview')
    else:
        form = ProfileForm()

    return render(request, 'profile_edit.html', {'form':profile_form})

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

