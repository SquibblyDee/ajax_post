from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

#  import our db
from .models import Post

def index(request):
    return render(request,'ajax_post_app/index.html')

def all_json(request):
    users = User.objects.all()
    return HttpResponse(serializers.serialize("json", users), content_type='application/json')

def all_html(request):
    return render(request, 'ajax_demo_app/all.html', { "users": User.objects.all() })

@csrf_exempt
def create(request):
    print(request.POST)
    Post.objects.create(text=request.POST['text'])
    return render(request, 'ajax_post_app/all.html',{ "posts": Post.objects.order_by("-id") })