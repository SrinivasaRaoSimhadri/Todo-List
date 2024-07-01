from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse
from task.models import *
from task.forms import *

@login_required
def tasks(request):
    if request.method=="POST":
        search = request.POST.get("search")
        tasks = Task.objects.filter(user = request.user).filter( Q(title__icontains = search))
        return render(request, "task/tasks.html" ,{"tasks":tasks})
    tasks = Task.objects.filter(user = request.user)
    return render(request, "task/tasks.html" ,{"tasks":tasks })

@login_required
def task(request , pk):
    task = Task.objects.get(id = pk)
    return render(request , "task/task.html" , {"task":task})

@login_required
def create(request):
    if request.method =="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("tasks")
    else:
        form = TaskForm()
    return render(request , "task/create.html" ,{"form":form})

@login_required
def update(request , pk):
    task = Task.objects.get(id = pk)
    if request.method =="POST":
        form = TaskForm(request.POST , instance=task)
        form.save()
        return redirect(reverse("task" , kwargs={"pk":pk}))
    else:
        form = TaskForm(instance=task)
    return render(request , "task/update.html" ,{"form" :form})

@login_required
def delete(request , pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return redirect("tasks")

def loginuser(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request , username = username  , password = password)
        if user == None:
            return render(request , "task/login.html" ,{"status" :"username or password is incorrect.."})
        else:
            login(request , user)
            return redirect("tasks")
    return render(request , "task/login.html")

def register(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        if password != password1 :
            print("pot metthos invked")
            return render(request , "task/register.html" ,{"status" :"verify your password.."})
        try:
            User.objects.create_user(username=username , password= password)
        except:
            return render(request , "task/register.html" ,{"status":"username already exists"})
        return redirect("loginuser")
    return render(request , "task/register.html")

def logoutuser(request):
    logout(request)
    return redirect("loginuser")