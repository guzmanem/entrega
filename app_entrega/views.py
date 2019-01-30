from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404


#def index(request):
#    template = loader.get_template('app_entrega/index.html')
#    context={}
#    return HttpResponse(template.render(context,request))

def index(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app_entrega/index.html', {'posts': posts}) 

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app_entrega/post_detail.html', {'post': post})