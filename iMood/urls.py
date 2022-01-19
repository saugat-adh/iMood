from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('user.api.urls')),
    path('moods/', include('mood.api.urls')),
    #path('medication/', include('medication.api.urls')),
]
