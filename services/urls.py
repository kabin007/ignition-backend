from django.urls import path, include
import user,course,university,country
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#url patterns for all the api's of the project
urlpatterns = [
    #user related api endpoint
    path('api/users/', include('user.urls')), 
    #university related api endpoint
    path('api/universities/', include('university.urls')), 
    #course related api endpoint
    path('api/courses/', include('course.urls')), 
    #country related api endpoint
    path('api/countries/', include('country.urls')),

    path('admin/',admin.site.urls),
]

if settings.DEBUG:  # Serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)