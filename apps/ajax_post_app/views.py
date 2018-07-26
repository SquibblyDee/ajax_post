from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

#  import our db
from .models import Post

def index(request):
    return render(request,'ajax_post_app/index.html',{ "posts": Post.objects.order_by("-id") })

@csrf_exempt
def create(request):
    print(request.POST)
    Post.objects.create(text=request.POST['text'])
    return render(request, 'ajax_post_app/all.html',{ "posts": Post.objects.order_by("-id") })