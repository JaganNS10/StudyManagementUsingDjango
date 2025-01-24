from django import forms
from .models import Register,UsersStudy

class registermodelform(forms.ModelForm):

    class Meta:

        model = Register

        fields = "__all__"

class usersstudymodelform(forms.ModelForm):
        class Meta:
             model = UsersStudy
             fields = ['study_name','study_description','study_phase','sponser_name']

class LoginForm(forms.Form):
     username = forms.CharField(max_length=255)
     password = forms.CharField(max_length=255,widget=forms.PasswordInput())

     