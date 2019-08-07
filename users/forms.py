from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('__init__')
        # self.fields['password1'].required = False
        #self.fields['password1'].widget = forms.HiddenInput()

    def clean(self):
        result = super().clean()
        print('cleaning')
        return result

    def save(self, commit=True):
        instance = super().save(commit=False)
        print('1', instance.email, instance.username)
        instance.set_unusable_password()
        print('1', instance.email, instance.username)
        instance.username = instance.email.split('@')[0]
        print('3', instance.email, instance.username)
        if commit:
            instance.save()
        return instance


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)
