from django import forms
from django.forms import fields, widgets
from django.urls.base import reverse
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import crispy_forms.layout as cfl
# import bcrypt


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")

        confirm_password = cleaned_data.get("confirm_password")
        # check password match before hashing
        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")
        # hash password
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'RegistrationForm'
        self.helper.form_class = 'bootstrap4'
        self.helper.form_method = 'POST'
        self.helper.form_action = '/create_user/'
        self.helper.attrs = {'novalidate': ''}
        self.helper.form_show_errors = True

        self.helper.add_input(Submit('submit', 'Register'))