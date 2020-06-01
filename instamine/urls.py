from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path(r'', views.index, name = "homepage"),
    path(r'search/', views.search_results, name='search_results'),
    path(r'image/(\d+)',views.image,name ='image'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)