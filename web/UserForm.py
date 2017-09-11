from django import forms

class UForm(forms.Form):
    username =forms.CharField(label='用户名', max_length=50, required='require')
    password = forms.CharField(label='密  码',max_length=20, required='require', widget=forms.PasswordInput())