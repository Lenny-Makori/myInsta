from django.shortcuts import render
from .models import Image, Profile
from .forms import ImageForm, ProfileForm

# Create your views here.
def index(request):
    image_display = '1 2 1 2 '

    return render(request, 'mainview/timeline.html', {"image_display":image_display})

def search_results(request):
    if 'userToFollow' in request.GET and request.GET['userToFollow']:
        search_term = request.GET.get("userToFollow")
        searched_user = Profile.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'mainview/search.html', {"message":message})
    else:
        message = "You haven't searched for any term"
        return render(request, 'mainview/search.html',{"message":message})


def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"mainview/image.html", {"image":image})

def profile(request):
    user_profile = Profile.get_profile(id=user_id)

    return render(request, 'profile.html', {'profile':profile})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')
    else:
        form = ImageForm()
    return render(request,'new_image.html',{'form':form})

