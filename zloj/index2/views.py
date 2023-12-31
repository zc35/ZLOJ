# -- coding: utf-8 --**
from django.shortcuts import render,HttpResponse,redirect
import pickle
import json
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=="POST":
        postdata=request.POST
        username = postdata.get("user")
        passwd = postdata.get("passwd")
        tf=open("users.json","r")
        users = json.loads(tf.read())
        flag=1
        for i in users:
            if i['name']==username:
                if i['password']==passwd:
                    rep = redirect('/')
                    rep.set_cookie('username', username)
                    print(username + ' login Accpted')
                    return rep
                else:
                    print(username + 'login password wrong')
                    return render(request,"login.html",{'warnings':'密码错误'})
        if flag==1:
            print('Notfound user' + username)
            return render(request,"login.html",{"warnings":'用户名未找到'})
def register(request):
    #print(request.method)
    if request.method=='GET':
        return render(request,'register.html',{'warnings':''})
    elif request.method == "POST":
        postdata=request.POST;
        username=postdata.get('user')
        passwd=postdata.get('passwd')
        with open('users.json',"rt") as tf:
           users=json.loads(tf.read())
        print(users)
        users[username]=passwd
        json_temp = json.dumps(users)
        with open('users.json',"w") as tf:
            tf.write(json_temp)
        rep = redirect('/')
        rep.set_cookie('username',username)
        print('register is Accepted '+username+' '+passwd)
        return rep;

def admin_index(request):
    if request.method == 'GET':
        return redirect('/')
    return render(request,'admin_index.html')