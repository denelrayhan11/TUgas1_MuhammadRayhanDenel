from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user = request.user)
    sudah_selesai = 0
    belum_selesai = 0
    for i in data_todolist :
        if i.finish == True:
            sudah_selesai+=1
        else:
            belum_selesai+=1
    if sudah_selesai>belum_selesai:
        info = "Selamat Kamu Rajin"
    else:
        info = "Ayo lebih giat lagi"
    context = {
        'task_list' : data_todolist,
        'nama' : request.user.username,
        'last_login' : request.COOKIES['last_login'],
        'info' : info,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    context = {}
    if request.method == "POST":
        temp = Task(user=request.user, title=request.POST.get('todo'),description=request.POST.get('description'))
        temp.save()
        return redirect('todolist:show_todolist')
    return render(request, "create-task.html",context)

def progres(request, pk):
    task_progres = Task.objects.get(id=pk)
    if (task_progres.finish == False):
        task_progres.finish = True
    else :
        task_progres.finish = False
    task_progres.save()

    return redirect('todolist:show_todolist')

def delete_task(request, pk):
    task_delete = Task.objects.filter(pk=pk)
    task_delete.delete()
    return redirect('todolist:show_todolist')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


# Create your views here.
