1.Initial setting on terminal  

```
$git clone git@github.com:xxxxsars/User_Register_Mail.git

$pip install  requirements.txt
```

2.Create your project and using managy.py to initial database
```
$startproject "your projectname"
$makemigration
$migrate
```

3.Copy file to your project

4.In setting.py INATALL_APP append "egister_email" like this
```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "register_email"
)


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# TLS Port
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'xxxxsars07@gmail.com'


# Application Key
EMAIL_HOST_PASSWORD = 'your gmail token'



```
5.On your urls.py  on urlpatterns list append your index page and named "index"
```python
"""
from django.conf.urls import url,include
from django.contrib import admin
from .views import here

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"user/",include('register_email.urls')),
    url('^$', here, name='index'),
]

```

6.On your project creat views.py

```python
def here(request):
    return  HttpResponse("HI welcome ")
```

7.Run server and connect 127.0.0.1:8000/user/register will show like this

![](https://github.com/xxxxsars/User_Register_Mail/blob/master/git_img/register_page.png?raw=true)
![](https://github.com/xxxxsars/User_Register_Mail/blob/master/git_img/confirm_page.png?raw=true)
![](https://github.com/xxxxsars/User_Register_Mail/blob/master/git_img/confirm_mail.png?raw=true)
