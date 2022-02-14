from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    
    path('password/reset/verify/', views.PasswordReset.as_view()),
    path('password/reset/verified/', views.PasswordFormpage.as_view(), name = 'password_reset_verified_page'),
    path('password/reset/success/', views.PasswordSuccess.as_view(), name = 'password_reset_success_page'),
    path('password/reset/error/', views.PasswordError.as_view(), name = 'password_reset_error_page'),
    
    path('email/change/verify/', views.EmailChangeVerifyFrontEnd.as_view()),
    path('email/change/error/', views.EmailChangeNotVerifiedFrontEnd.as_view(), name = 'email_change_not_verified_page'),
    path('email/change/verified/', views.EmailChangeVerifiedFrontEnd.as_view(), name = 'email_change_verified_page'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
