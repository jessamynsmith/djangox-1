from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        helper = self.helper = FormHelper()
        layout = helper.layout = Layout()
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.fields['password1'].label = 'TEST'
        self.fields['password1'].widget.attrs['placeholder'] = 'TEST'
        print(self.fields['password1'].widget.attrs)
        layout.append(
            Field('password1', placeholder='THIS IS YOUR PASSWORD')
        )
        #for field_name, field in self.fields.items():
        #    layout.append(Field(field_name, placeholder=field.label))
        helper.form_show_labels = False

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)
