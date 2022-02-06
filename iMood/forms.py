from django import forms
from django.forms.forms import NON_FIELD_ERRORS

class AddErrorMixin(object):
    def add_error(self, field, msg):
        field = field or NON_FIELD_ERRORS
        if field in self._errors:
            self._errors[field].append(msg)
        else:
            self._errors[field] = self.error_class([msg])

class PasswordResetVerifiedForm(AddErrorMixin, forms.Form):
    password = forms.CharField(label = 'password')
