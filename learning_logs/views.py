from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic
from .forms import TopicForm

# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request,'learning_logs/index.html')
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未提交数据：创建一个新表单
        form = TopicForm()
    else:
        #POST提交的新数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

def topic(request,topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)