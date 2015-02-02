# Create your views here.

from django.shortcuts import render_to_response

def index(request):
   template_values = {}

   return render_to_response('index.html', template_values)
