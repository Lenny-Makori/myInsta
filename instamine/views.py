from django.shortcuts import render

# Create your views here.
def index(request):
    image_display = 'APP TEST, 1 2 1 2'

    return render(request, 'mainview/timeline.html', {"image_display":image_display})