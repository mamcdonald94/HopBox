from django import forms
from django.forms import fields, widgets
from django.urls.base import reverse
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, HTML
from crispy_forms.bootstrap import FormActions


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'password', 'address')
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
        self.helper.form_action = '/register/create-user/'
        self.helper.attrs = {'novalidate': ''}
        self.helper.form_show_errors = True
        self.helper.layout = Layout(
            Fieldset(
                'Register Here!',
                'firstname',
                'lastname',
                'email',
                'password',
                'confirm_password',
                HTML("""
                    <p>Please input your preferred shipping address!</p>
                """),
                'address'
            ),
            FormActions(
                Submit('submit', 'Register', css_class='btn-success')
            ),
        )

class EditAccountForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'password', 'address')
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super(EditAccountForm, self).clean()
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
        self.helper.form_id = 'EditAccountForm'
        self.helper.form_class = 'bootstrap4'
        self.helper.form_method = 'POST'
        self.helper.form_action = '/update-account/'
        self.helper.attrs = {'novalidate': ''}
        self.helper.form_show_errors = True
        self.helper.layout = Layout(
            Fieldset(
                'Edit Account Info!',
                'firstname',
                'lastname',
                'email',
                'password',
                'confirm_password',
                'address'
            ),
            FormActions(
                Submit('submit', 'Update Account', css_class='btn-success')
            ),
        )