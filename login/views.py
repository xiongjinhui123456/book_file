from django.shortcuts import render, HttpResponse

# Create your views here.
from login import models


def logon(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        try:
            x = models.User.objects.get(username=u)
            if x.password == p:
                return render(request, "index.html")
            else:
                return HttpResponse("密码错误")
        except:
            return HttpResponse("用户名不存在")

        # return HttpResponse("主页")
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        try:
            x = models.User.objects.get(username=u)
            return HttpResponse("用户名已存在")
        except:
            new_user = models.User.objects.create()
            new_user.username = u
            new_user.password = p
            new_user.save()
            return HttpResponse("注册成功")
        else:
            return HttpResponse("未知错误")
    return render(request, "register.html")


def index(request):
    return HttpResponse("主页")


from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from login.models import User


# Create your views here.
class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        rname = request.POST.get("rname")
        rpasswd = request.POST.get("rpasswd")

        # 注册成功跳转到到登录页面，注册加判断已经存在提示改用用户已存在
        users = User.objects.all()
        for i in users:
            if rname == i.name:
                return HttpResponse("用户已存在")
        try:
            User.objects.create(name=rname, password=rpasswd)
        except Exception as e:
            print(e)
            return HttpResponse("注册失败")

        return redirect('/login/')


# 类视图---登录模板
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        lname = request.POST.get("lname")
        lpasswd = request.POST.get("lpasswd")

        # 登录失败时需要提示是用户名不存在还是密码错误
        try:  # 存放可能出现异常的代码 查询数据多个条件时默认是并且的关系
            user = User.objects.get(name=lname)
            # 当输入的用户名在数据库里查询不到，说明try里面的代码存在异常
            # 执行万能异常里面的语句
        except Exception as e:  # 捕获异常将异常存到e里
            print(e)
            return HttpResponse("用户名不存在")

        # 如果用户名对，就判断密码有没有输入正确
        if lpasswd != user.password:
            return HttpResponse("用户名和密码不匹配")

        return redirect('/add/')