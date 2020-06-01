from django.shortcuts import render
from .models import Image, Profile

# Create your views here.
def index(request):
    image_display = Image.objects.all()

    return render(request, 'mainview/timeline.html', {"image_display":image_display})

def search_results(request):

    return render(request, 'mainview/search.html')

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"mainview/image.html", {"image":image})