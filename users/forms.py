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
        print(self.fields['password1'].widget.attrs)
        layout.append(
            Field('password1', placeholder='THIS IS YOUR PASSWORD')
        )
        #for field_name, field in self.fields.items():
        #    layout.append(Field(field_name, placeholder=field.label))
        del self.fields['password1']
        del self.fields['password2']
        helper.form_show_labels = False

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = super(UserCreationForm, self).clean_password2()
        if bool(password1) ^ bool(password2):
            raise forms.ValidationError("Fill out both fields")
        return password2


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email')
