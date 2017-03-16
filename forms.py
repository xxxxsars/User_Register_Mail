from django import  forms
from captcha.fields import ReCaptchaField
from django.contrib.auth.models import User

class RegisterForm(forms.Form):


    username = forms.CharField(max_length=40,required=True,label="用戶名稱",error_messages={'required':'請填入用戶資料',"invalid":"請填入正確用戶資料"})
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={"id":"password"}),label="用戶密碼",error_messages={"require":'請填入用密碼',"invalid":"請填入正確用戶密碼"})
    repeatPassword = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"id": "repeatPassword"}),label="再次輸入密碼",error_messages={'required':'請重複輸入用戶密碼',"invalid":"請填入正確密碼確認資料"})
    email = forms.EmailField(required=True,label="電子郵件",error_messages={'required':'請填入用戶信箱',"invalid":"請填入正確用戶信箱"})



    def clean_username(self):
        #clean_data為驗上方證過的資料取出資料後作為參數
        username  = self.cleaned_data['username']
        if len(username)<5:
            raise forms.ValidationError("使用者名稱不得少於四字元")
        elif User.objects.filter(username=username).count():
            raise  forms.ValidationError("此帳號已註冊過！")
        return username


    def clean_password(self):
        password = self.cleaned_data['password']

        if  len(password)<8 :
            raise forms.ValidationError("密碼不得少於８字元！")
        return password

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).count():
            raise forms.ValidationError("此信箱已註冊過！")
        return email





class ConfirmMailForm(forms.Form):
    email_token = forms.CharField(required=True, max_length=4)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, required=True, label="用戶名稱",
                               error_messages={'required': '請填入用戶資料', "invalid": "請填入正確用戶資料"})
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"id": "password"}), label="用戶密碼",
                               error_messages={"require": '請填入用密碼', "invalid": "請填入正確用戶密碼"})

    def clean_username(self):
        self.username=self.cleaned_data['username']

        self.users = []
        for user in User.objects.values_list():
            self.users.append(user[4])

        if self.username not in self.users:
            raise forms.ValidationError("帳號未註冊，請重新註冊後登入")
        return self.username

    def clean_password(self):

        if self.username in self.users:
            vaild = User.check_password(User.objects.get(username=self.username),self.cleaned_data['password'])
            if  not vaild:
                raise forms.ValidationError("密碼錯誤請重新輸入")
            return vaild



