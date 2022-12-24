from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse
def insert_topic(request):
    form=TopicForm()
    d={'form':form}
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('insert the data into topic model')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    form=WebpageForm()
    d={'form':form}
    if request.method=='POST':
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('insert the data into webpage model')
    return render(request,'insert_webpage.html',d)


def insert_AccessRecords(request):
    form=AccessRecordsForm()
    d={'form':form}
    if request.method=='POST':
        form_data=AccessRecordsForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('insert the data into webpage model')
    return render(request,'insert_AccessRecords.html',d)