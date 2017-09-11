from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$', views.login, name='Login'),
    url(r'^index/$', views.index, name='index'),
    url(r'^loginout/$', views.login_out, name='loginout'),
    url(r'^main/$',views.table, name='main'),
]