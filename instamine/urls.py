from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.index, name = "homepage"),
    path('search/', views.search_results, name='search_results'),
    path('image/(\d+)',views.image,name ='imageview'),
    path('new/image', views.new_image, name='new_image'),
    path('profile/<user_id>', views.profile, name='profileview'),
    path('profile/edit/', views.update_profile, name = 'profileedit'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)