from allauth.account.views import SignupView

from users.forms import CustomUserCreationForm


class MySignupView(SignupView):
    form_class = CustomUserCreationForm

    # def get_form_class(self):
    #     return get_form_class(app_settings.FORMS, 'signup', self.form_class)

    def dispatch(self, request, *args, **kwargs):
        print('MySignupView')
        response = super().dispatch(request, *args, **kwargs)
        return response
