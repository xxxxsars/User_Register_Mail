from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.contrib import auth
from django.contrib.auth.models import User

from django.contrib import messages
from .forms import RegisterForm,LoginForm,ConfirmMailForm

#將url定義的name轉回網址
from django.core.urlresolvers import reverse

#寄信模組所需
import string
import random
from django.core.mail import send_mail
from django.template import loader



#產生四位驗證碼
def id_grenerator(size=4,char = string.ascii_uppercase+string.digits):
        return ''.join(random.choice(char) for _ in range(size))
class Register():
    def __init__(self):
        self.username = ''
        self.password = ''
        self.email=""
        self.confirm=''
        self.send_token = ''


    def register(self,request):
    # 檢查用戶有否發出POST請求
        if request.method == "POST":




            # 從表單裡取得request裡的Post參數
            f = RegisterForm(request.POST)

            # 若表單的所有欄位皆填寫正確，取得裡面的資料
            if f.is_valid():
                self.username = request.POST['username']
                self.password = request.POST["password"]
                self.email = request.POST['email']

                # 透過xxxxsars07來寄送驗證信件
                user_mail_topic = '感謝您註冊本網站'
                user_messgae = '內容'
                # 要寄送的對象，可以多個對象
                to_list = [self.email, ]
                self.confirm = id_grenerator()
                html_message = loader.render_to_string('Mail_temp.html', locals())
                # Send User Email STMP(mail use your register in google's mail and input its token on server)
                send_mail(user_mail_topic,user_messgae,'xxxxsars07@gmail.com', to_list,fail_silently=False, html_message=html_message)

                self.send_token = id_grenerator(8)


                # user = User.objects.create_user(self.username, self.email, self.password)
                # user.save()
                # account = auth.authenticate(username=self.username, password=self.password)
                # auth.login(request, account)
                # susessful  ="註冊成功！3秒後跳回登入頁面"
                #return render(request, 'register_mail.html',locals())
                return HttpResponseRedirect(reverse("mail_confirm"))



         #若用戶並沒有發出POST請求，傳送之前建立的RegisterForm至註冊頁面
        else:
            f= RegisterForm()
            if request.user.is_authenticated():
                username = request.user.username
        return render(request,'register_mail.html',locals())

    def comfirm_mail(self,request):

        if len(self.send_token)==8:
            if request.method =="POST":
                f = ConfirmMailForm(request.POST)

                if f.is_valid():
                    email_token = request.POST['email_token']
                    if email_token ==self.confirm:
                        user = User.objects.create_user(self.username, self.email, self.password)
                        user.save()
                        account = auth.authenticate(username=self.username, password=self.password)
                        auth.login(request, account)
                        susessful = "註冊成功！3秒後跳回登入頁面"
                        return render(request,'Comfirm_mail.html',locals())
                    else:
                        messages.error(request,"驗證碼錯誤請重新輸入")
                        return render(request,'Comfirm_mail.html',locals())

            else:
                f = ConfirmMailForm()
            return render(request,"Comfirm_mail.html",locals())

        else:
            messages.error(request, "從重新註冊後再收取驗證碼！")
            f  = RegisterForm()

            # return render(request,"register_mail.html",locals())
            return HttpResponseRedirect(reverse("register"))

        # user = User.objects.create_user(self.username, self.email, self.password)
        # user.save()
        # account = auth.authenticate(username=self.username, password=self.password)
        # auth.login(request, account)
        # susessful = "註冊成功！3秒後跳回登入頁面"
        #
        # return render(request,'Comfirm_mail.html',locals())


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))


    elif request.method == "POST":

        # 從表單裡取得request裡的Post參數
        f = LoginForm(request.POST)

        # 若表單的所有欄位皆填寫正確，取得裡面的資料
        if f.is_valid():
            #
            username = request.POST['username']
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                 return render(request,'login.html',locals())

    else:
        f = LoginForm()
    return render(request,'login.html',locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))


