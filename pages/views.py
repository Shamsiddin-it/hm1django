from django.http import HttpResponse
from django.template import loader

# Create your views here.

def homePageView(request):
    template = loader.get_template("html.html")
    return HttpResponse(template.render())
