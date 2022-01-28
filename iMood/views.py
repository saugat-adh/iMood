from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from authemail import wrapper
import requests

class SignupVerifyFrontEnd(View):
    def get(self, request, format=None):
        code = request.GET.get('code', '')

        response = requests.get('http://imood-web-api.herokuapp.com/account/signup/verify/?code=' + code, params=request.GET)

        # Handle other error responses from API
        if response.status_code==200:
            return HttpResponseRedirect(reverse('signup_verified_page'))

        return HttpResponseRedirect(reverse('signup_not_verified_page'))


class SignupVerifiedFrontEnd(TemplateView):
    template_name = 'verified_page.html'


class SignupNotVerifiedFrontEnd(TemplateView):
    template_name = 'unverified_page.html'
