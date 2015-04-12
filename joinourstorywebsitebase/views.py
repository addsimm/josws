# Create your views here.
from __future__ import print_function
from google.appengine.api import users
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from joinourstorywebsitebase.models import *


def index(request):
   template_values = {}
   template_values.update({'page_name': 'Landing Page'
                           })

   return render_to_response('index.html', template_values)


def contactus(request):
    template_values = {}
    template_values.update(csrf(request))
    template_values.update({'page_name': 'Contact Us'
                            })
    if request.method == 'POST':
        ### FOR DEBUG raise KeyError(request.POST)
        joscontactmessage = JOSContactMessage(parent = JOSContactMessageSSS_key())

        if users.get_current_user():
            joscontactmessage.jcm_sender = users.get_current_user()

        joscontactmessage.jcm_first_name = request.POST['firstnamefield']
        joscontactmessage.jcm_last_name = request.POST['lastnamefield']
        joscontactmessage.jcm_email_address = request.POST['emailfield']
        joscontactmessage.jcm_message = request.POST['messagefield']

        print("joscontactmessage:", joscontactmessage.jcm_message)


        #joscontactmessage.put()

    # template_values = return_template_values(path) #implement

    return render_to_response('contactus.html', template_values)
