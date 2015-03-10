from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import HttpResponse
from .forms import TaskForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import Task, AppUser


def index(request):
    tasks = Task.objects.all()
    return render_to_response("app/index.html", {"tasks": tasks}, context_instance=RequestContext(request))
    # return render(request,'index.html')


def about(request):
    # tasks = Task.objects.all()
    # return render_to_response("resp.html", {"tasks": tasks})
    return render(request, 'app/about.html', context_instance=RequestContext(request))


def task(request):
    tasks = Task.objects.all()
    # return render_to_response("app/task.html", {"tasks": tasks},context_instance=RequestContext(request))

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            task_name = cd['TaskName']
            task_Type = cd['TaskType']
            task_Count = cd['TaskCount']
            task_State = cd['TaskState']
            creator = AppUser.objects.get(id=1)
            deviceType = cd['DeviceType']
            description = cd['Description']
            createTime = cd['CreateTime']
            updateTime = cd['UpdateTime']
            createWay = cd['CreateWay']
            isShared = cd['IsShared']
            task = Task(TaskName=task_name, TaskType=task_Type, TaskCount=task_Count, TaskState=task_State,
                        Creator=creator, DeviceType=deviceType, Description=description, CreateTime=createTime,
                        UpdateTime=updateTime, CreateWay=createWay,
                        IsShared=isShared)

            task.save()
            # id = Task.objects.order_by('-publish_time')[0].id
            return HttpResponseRedirect('http://www.baidu.com')
    else:
        form = TaskForm()
    return render_to_response('app/task.html', {'tasks': tasks, 'form': form}, context_instance=RequestContext(request))