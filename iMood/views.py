from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.views.generic.base import View
from authemail import wrapper
import requests

import json

from .forms import PasswordResetVerifiedForm

url = 'https://imood-web.azurewebsites.net/account/signup/verify/?code='

class SignupVerifyFrontEnd(View):
    def get(self, request, format=None):
        code = request.GET.get('code', '')

        response = requests.get(url + code, params=request.GET)

        # Handle other error responses from API
        if response.status_code==200:
            return HttpResponseRedirect(reverse('signup_verified_page'))

        return HttpResponseRedirect(reverse('signup_not_verified_page'))


class SignupVerifiedFrontEnd(TemplateView):
    template_name = 'verified_page.html'


class SignupNotVerifiedFrontEnd(TemplateView):
    template_name = 'unverified_page.html'


class PasswordReset(View):
    def get(self, request, format=None):
        code = request.GET.get('code', '')

        response = requests.get(url + code, params=request.GET)

        # Handle other error responses from API
        if response.status_code==200:
            request.session['password_reset_code'] = code
            return HttpResponseRedirect(reverse('password_reset_verified_page'))

        return HttpResponseRedirect(reverse('password_reset_error_page'))

class PasswordError(TemplateView):
    template_name = 'password_error_page.html'
    
    
class PasswordSuccess(TemplateView):
    template_name = 'password_success_page.html'
    
    
class PasswordFormpage(FormView):
    template_name = 'password_verified_page.html'
    form_class = PasswordResetVerifiedForm
    success_url = reverse_lazy('password_reset_success_page')
    

    def form_valid(self, form):
        code = self.request.session['password_reset_code']
        password = form.cleaned_data['password']
        
        params = {
            "code" : code,
            "password" : password,
        }
        
        response = requests.post(url, data=params)
        
        if response.status_code==200:
            return HttpResponseRedirect(reverse('password_reset_success_page'))

        return HttpResponseRedirect(reverse('password_reset_error_page'))




class EmailChangeVerifyFrontEnd(View):
    def get(self, request, format=None):
        code = request.GET.get('code', '')

        response = requests.get(url + code)

        # Handle other error responses from API
        if response.status_code==200:
            return HttpResponseRedirect(reverse('email_change_verified_page'))

        return HttpResponseRedirect(reverse('email_change_not_verified_page'))
    
    
class EmailChangeVerifiedFrontEnd(TemplateView):
    template_name = 'email_change_verified.html'


class EmailChangeNotVerifiedFrontEnd(TemplateView):
    template_name = 'email_change_error.html'