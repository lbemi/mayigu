from django.shortcuts import render,render_to_response, get_list_or_404, redirect
from django.http import  HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .UserForm import UForm
from .models import user_info


# def Login(request):
#     return render(request, 'html_web/Login.html', context={
#         'Login_title':'麻衣谷仓管系统'
#     })



def login(request):
    if request.method == 'POST':
        uf = UForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = user_info.objects.filter(user_name__exact=username,user_pwd__exact=password)
            if user:
                response = HttpResponseRedirect('/index/')
                response.set_cookie('username', username, 3600)
                return response
            else:
                return HttpResponseRedirect('/login/',{'errmesg':'账号密码错误'})
    else:
        uf = UForm()
    # return render(request,'html_web/Login.html',{'uf':uf},context=HttpResponse(request))

    return HttpResponse(render(request,'html_web/Login.html', {'uf':uf},{'errmesg':'账号密码错误'}))

def index(req):
    username = req.COOKIES.get('username', '')
    return render_to_response('html_web/index.html', {'username':username})

def login_out(req):
    response = HttpResponseRedirect('/login/')
    response.delete_cookie('username')
    return response