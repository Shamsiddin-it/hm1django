from django.http import HttpResponse
from django.template import loader

# Create your views here.

def homePageView(request):
    template = loader.get_template("html.html")
    return HttpResponse(template.render())

def homePageView2(request):
    template = loader.get_template("html2.html")
    return HttpResponse(template.render())

def homePageView3(request):
    template = loader.get_template("html3.html")
    return HttpResponse(template.render())
