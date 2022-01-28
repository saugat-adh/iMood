from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('user.api.urls')),
    path('moods/', include('mood.api.urls')),
    path('medication/', include('medication.api.urls')),
    
    
    path('signup/verify/', views.SignupVerifyFrontEnd.as_view()),
    path('signup/verified/', views.SignupVerifiedFrontEnd.as_view(),
         name='signup_verified_page'),
    path('signup/not_verified/', views.SignupNotVerifiedFrontEnd.as_view(),
         name='signup_not_verified_page'),
]
