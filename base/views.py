from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def register(request):
     if request.method=='POST':
          username=request.POST['username']
          password=request.POST['password']
          print(username,password)

          allusername=[]
          alluser=User.objects.all()
          for i in alluser:
               allusername+=[i.username]
          username_ex=False
          if username in  allusername:
               username_ex=True
               return render (request,'reg.html',{'username_ex':username_ex})
          else:
            User.objects.create(username=username,password=password)
            return redirect ('login')
     return render (request,'reg.html')




def login_a(request):
     if request.method=='POST':
          username=request.POST['username']
          password=request.POST['password']
          # print(username,password)
          # user = authenticate(username=username,password=password)
          # print(user)
          try:
               user=User.objects.get(username=username)
          except:
               return HttpResponse(' username doesnot exist')
          if user.password==password:
               login(request,user)
               return redirect('home')
          else:
               return HttpResponse('wrong')
     return render(request,'login.html')




def logout_a(request):
     logout(request)
     return redirect ('login')




def forget_p(request):
   

     return render(request,'for_p.html')



