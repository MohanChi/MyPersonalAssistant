from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from AssistantApp.models import *
from django.http import JsonResponse
from datetime import datetime

# Create your views here.

def index(request):
    template = loader.get_template('AssistantApp/main.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    if request.method == "GET":
        if request.session.get('is_login'): #already login
            return redirect('/AssistantApp/new-task')
        else:
            template = loader.get_template('AssistantApp/login.html')
            context = {}
            return HttpResponse(template.render(context, request))
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "cmh" and password == "123456":
            request.session['is_login'] = True
            request.session['username'] = username
            print("loginininininin-post-redirect-newtask")
            return redirect('/AssistantApp/new-task')
        else:
            template = loader.get_template('AssistantApp/login.html')
            context = {}
            return HttpResponse(template.render(context, request))

def logout(request):
    request.session.flush()
    return redirect("/AssistantApp/")

def new_task(request):
    if request.method == "GET":
        if request.session.get('is_login'):
            template = loader.get_template('AssistantApp/newtask.html')
            context = {'username': request.session["username"]}
            return HttpResponse(template.render(context, request))
        else:
            return redirect('/AssistantApp/login')
    elif request.method == "POST":
        if request.session.get('is_login'):
            data = request.POST
            task = task_Model()
            task.taskname = data.get('taskname', '')
            if data.get('due','') == '':
                task.due = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                task.due = data.get('due', '')
            task.priority = data.get('priority', '')
            task.type = data.get('type', '')
            task.difficulty = data.get('difficulty', '')
            task.detail = data.get('detail', '')
            task.visible = data.get('visible', '')
            task.save()
            print("newtask-post-redirect-agenda")
            return redirect('/AssistantApp/agenda')
        else:
            return redirect('/AssistantApp/login')

def edit_task(request):
    if request.method == "GET":
        template = loader.get_template('AssistantApp/newtask.html')
        task = task_Model.objects.get(id=request.GET.get('id'))
        context = {'username': request.session["username"], 'task': task}
        return HttpResponse(template.render(context, request))
    else:
        data = request.POST
#         print(data)
#         print("1111111111111", data.get('taskname', ''))
        t = task_Model.objects.get(id=request.POST.get('id'))
        t.taskname = data.get('taskname', '')
        t.due = data.get('due', '')
        t.priority = data.get('priority', '')
        t.type = data.get('type', '')
        t.difficulty = data.get('difficulty', '')
        t.detail = data.get('detail', '')
        t.visible = data.get('visible', '')
        t.save()
        print("edit-post-redirect-agenda")
        return redirect('/AssistantApp/agenda')

def agenda(request):
        if request.method == "POST":
            print(request.POST.get('id'))
            task_Model.objects.get(id=request.POST.get('id')).delete()
            return JsonResponse({'status':'success'}, status=200)
        elif request.method == "GET":
              if request.session.get('is_login'):
                  template = loader.get_template('AssistantApp/agenda.html')
                  tasklist_obj = task_Model.objects.all()
                  context = {'username': request.session["username"], 'tasklist':tasklist_obj}
                  return HttpResponse(template.render(context, request))
              else:
                  return redirect('/AssistantApp/login')

def show_task(request):
    template = loader.get_template('AssistantApp/showtask.html')
    task = task_Model.objects.get(id=request.GET.get('id'))
    context = {'username': request.session["username"], 'task': task}
    return HttpResponse(template.render(context, request))