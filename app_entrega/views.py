from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


#def index(request):
#    template = loader.get_template('app_entrega/index.html')
#    context={}
#    return HttpResponse(template.render(context,request))

def index(request):
    return render(request, 'app_entrega/index.html', {})