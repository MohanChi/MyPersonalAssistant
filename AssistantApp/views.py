from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from AssistantApp.models import *
from django.http import JsonResponse
from datetime import datetime
import requests
import json
# from getmac import get_mac_address as gma

# Create your views here.

def index(request):
#     task_Model.objects.all().delete()
#     User.objects.all().delete()
    template = loader.get_template('AssistantApp/main.html')
    category = ''
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'Zf+5oCDSXry8Eo15++PzeQ==RS4UwzQeJ2KBxAFm'})
    if response.status_code == requests.codes.ok:
         print(response.text)
    else:
         print("Error:", response.status_code, response.text)
    res_json = response.json()
    print(res_json[0].get('quote'))
    context = {'quote': res_json[0].get('quote'), 'author': res_json[0].get('author')}
    return HttpResponse(template.render(context, request))

def register(request):
    if request.method == "GET":
        template = loader.get_template('AssistantApp/Register.html')
        context = {}
        return HttpResponse(template.render(context, request))
    else:
        userid = request.POST.get("userid")
        password = request.POST.get("pwd")

        User.objects.create(username=userid, password=password)
        result = User.objects.filter(username=userid)
        if result.exists():
            template = loader.get_template('AssistantApp/Register.html')
            context = {"error_msg": "User id already exists, please re-enter or go to the login page"}
            return HttpResponse(template.render(context, request))
        else:
            return redirect('/AssistantApp/login')

def login(request):
    if request.method == "GET":
        if request.session.get('is_login'): #already login
            return redirect('/AssistantApp/new-task')
        else:
            template = loader.get_template('AssistantApp/login.html')
            context = {}
            return HttpResponse(template.render(context, request))
    elif request.method == "POST":
        username_post = request.POST.get("username")
        password_post = request.POST.get("password")
        print(username_post)
        user = User.objects.get(username=username_post)
        print(user.password)
        if password_post == user.password:
#         if username == "cmh" and password == "123456":
            request.session['is_login'] = True
            request.session['username'] = username_post
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

    category = ''
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'Zf+5oCDSXry8Eo15++PzeQ==RS4UwzQeJ2KBxAFm'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

#     google map api
    url = 'https://maps.googleapis.com/maps/api/staticmap?'
    center = "Lafayette"
    zoom = '10'
    size = '400x350'
    api_key = 'AIzaSyCf0T-bho9t6moCVd_EmfB3xfUbmV1C3Ac'
    response = requests.get(url + "key=" + api_key + "&center=" + center
                            + "&zoom=" + zoom + "&size="+ size
                             + "&sensor=false")
    print(url + api_key + "&center=" + center + "&zoom=" + zoom + "&size="+ size + "&sensor=false")
#     print("response:!!!!!!: ", response.content)

    context = {'username': request.session["username"], 'task': task, 'mapImage': response.content}

    return HttpResponse(template.render(context, request))

