from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    index_topics = {"content":"This is the content of the Topic Page"}
    return render(request,'topics/index.html',context=index_topics)
