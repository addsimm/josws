# Create your views here.

from google.appengine.api import users
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from joinourstorywebsitebase.models import *

def index(request):
   template_values = {}

   return render_to_response('index.html', template_values)


def contactus(request):
    template_values = {}
    if request.method == 'POST':
        joscontactmessage = JOSContactMessage(parent = JOSContactMessageSSS_key())  # finicky

        if users.get_current_user():
            joscontactmessage.jcm_sender = users.get_current_user()
        else:
            joscontactmessage.jcm_sender = "unknown"


        # implement
        joscontactmessage.dd_url = request.POST.get('url')

        joscontactmessage.put()
        return # ??

    page_name = 'Contact Us'



    # template_values = return_template_values(path) #implement
    # template_values.update(csrf(request))
    # template_values.update({'page_name': page_name,
    #                         'discussedDocs': discussed_docs,
    #                         'currentDocs': current_docs
    # })

    return render_to_response('contactus.html', template_values)
