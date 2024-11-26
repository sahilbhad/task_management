from django.http import HttpResponse
from django.shortcuts import render, redirect
from  django.db.models import Q
from myapp.models import Task, HistoryTask ,completed
from .forms import TaskForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    # a=Task.objects.all()
    # a=Task.objects.get(id=2)
                  #get ,#filter #complexdata  #var is model instans 



    a=[]
    n=False
    if request.method=="GET":
        if 'search' in request.GET:
            c=request.GET['search']
            print(c)
            a = Task.objects.filter(Q(host_id=request.user) & (Q(title__icontains=c) | Q(desc__icontains=c)))
            if len(a)==0:
                n=True
        else:
             a=Task.objects.filter(host_id=request.user)       
         
    return render(request, 'home.html',{'a':a,'n':n})

def add_task(request):
    

    print("hello")
    print(request)
    print(request.method)
    print(request.GET)

    # if 'title' in request.GET:
    #     title_data=request.GET['title']
    #     content=request.GET['content']
    #     print(title_data,content)


      
    print("hello")        #hello
    print(request)         #<WSGIRequest: POST '/addtask/'>
    print(request.method)  #GET by  defult 
    print(request.GET)      #<QueryDict: {}>
    print(request.POST)  

    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        Task.objects.create(title=title, desc=desc,host_id=request.user)
        return redirect('home')
    return render(request, 'add_task.html')

def history(request):
    b=HistoryTask.objects.all()
    return render(request, 'history.html',{'b':b})

def aboutus(request):
    return render(request, 'about.html')




def upd(request, id):
    a=Task.objects.get(id=id)
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        # print(title)
        # print(desc)
        a.title=title
        a.desc=desc
        a.save()
        return redirect('home')
    return render(request, 'add_task.html', {'a':a})





def dele(request, id):
    a=Task.objects.get(id=id)
    if request.method=='POST':
        HistoryTask.objects.create(title=a.title,desc=a.desc,host_id=request.user)
        a.delete()
        return redirect('home')
    return render(request, 'dele.html',{'a':a})



def details(request,id):
    a=Task.objects.get(id=id)
    return render(request,'detail.html',{'a':a})




def clear(request):
    a=HistoryTask.objects.all()
    a.delete()
    return redirect('history')
    

    
def Restoreall(request):
    
    a=HistoryTask.objects.all()
    
    for i in a:
        print(i.title,i.desc)
        Task.objects.create(title=i.title,desc=i.desc,host_id=request.user)
    a.delete()
    return redirect('home')
    


def restore(request, id):
    b=HistoryTask.objects.get(id=id)
    Task.objects.create(title=b.title, desc=b.desc,host_id=request.user)
    b.delete()
    return redirect('home')



def delet(request, id):
    b=HistoryTask.objects.get(id=id)
    b.delete()
    return redirect('history')

                            

def completed_a(request,id):
    a=Task.objects.get(id=id)
    completed.objects.create(title=a.title,desc=a.desc,host_id=request.user)
    a.delete()
    return redirect('home')



def tc(request):
    a=completed.objects.all()
    return render(request, 'completed.html',{'a':a})



def Restoreall_tc(request):
    t = completed.objects.all()
    
    for i in t:
        Task.objects.create(title=i.title, desc=i.desc,host_id=request.user)
    
    completed.objects.all().delete()
    
    return redirect('home')



def notc(request, id):
    c=completed.objects.get(id=id)
    Task.objects.create(title=c.title, desc=c.desc,host_id=request.user)
    c.delete()
    return redirect('home')



def contacts(request):
        if request.method=='POST':
            f=TaskForm(data=request.POST)
            if f.is_valid():
                f.save()

        return render(request, 'contacts.html',{'TaskForm':TaskForm})






def profile(request):
    user = request.user 
    return render(request ,'profile.html',{'user':user})


def e_p(request,id):
    a=User.objects.get(id=id)
    if request.method=='POST':
        a.username=request.POST['username']
        a.password=request.POST['password']
        a.save()
        return redirect('login')
    return render(request ,'e_p.html',{'a':a})


def delete_p(request,id):
    a=User.objects.get(id=id)
    a.delete()
    return redirect('reg')
    