from django.shortcuts import render,render_to_response, get_list_or_404, redirect
from django.http import  HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from .models import user_info


# def Login(request):
#     return render(request, 'html_web/Login.html', context={
#         'Login_title':'麻衣谷仓管系统'
#     })

class UserForm(forms.Form):
    username =forms.CharField(label='u', max_length=50)
    password = forms.CharField(label='p',max_length=20, widget=forms.PasswordInput())

def login_web(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # username = uf.cleaned_data['u']
            username = request.POST.get('u','')
            password = request.POST.get('p','')
            # password = uf.cleaned_data['p']
            user = user_info.objects.filter(user_name__exact=username,user_pwd__exact=password)
            if user:
                response = HttpResponseRedirect('html_web/index.html')
                # response = redirect('html_web/index.html')
                response.set_cookie('username', username, 3600)
                return response
            else:
                return HttpResponseRedirect('html_web/Login.html', context={
            'Login_title': '麻衣谷仓管系统'})
        else:
            uf = UserForm()
        return render_to_response('html_web/index.html')
    else:
        return render(request, 'html_web/Login.html', context={
            'Login_title': '麻衣谷仓管系统'})


def index(req):
    username = req.COOKIES.get('username', '')
    return render_to_response('index.html', {'username':username})