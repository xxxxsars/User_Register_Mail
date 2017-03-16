from django.conf.urls import include,url
from .views import login,logout,Register

r = Register()
urlpatterns = [
    url(r'^register/', r.register,name='register'),
    url(r'^login/',login,name="login"),
    url('^logout/',logout,name='logout'),
    url(r'^confirm/', r.comfirm_mail,name='mail_confirm'),
]

