from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile


class SignupForm(UserCreationForm):
    # email = forms.EmailField(error_messages='Hello')

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'profile_pic',
                  'username', 'password1', 'password2']


class DashboardForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'profile_pic',
                  'username']

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
        try:
            username = Profile.objects.exclude(
                pk=self.instance.pk).get(username=username)
        except Profile.DoesNotExist:
            return username
        raise forms.ValidationError('This username is already in use.')

    # def clean_email(self):
    #     if self.is_valid():
    #         email = self.cleaned_data['email']
    #     try:
    #         email = Profile.objects.exclude(
    #             pk=self.instance.pk).get(email=email)
    #     except Profile.DoesNotExist:
    #         return email
    #     raise forms.ValidationError('This email is already in use.')
