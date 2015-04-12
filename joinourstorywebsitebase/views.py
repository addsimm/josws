# Create your views here.
from __future__ import print_function

from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from joinourstorywebsitebase.models import *

from google.appengine.api import users
from google.appengine.api import mail


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

        joscontactmessage.jcm_message = request.POST['messagefield']

        user_email_address = request.POST['emailfield']
        print("joscontactemail:", joscontactmessage.jcm_message)


        if mail.is_email_valid(user_email_address):
            joscontactmessage.jcnm_email_address = user_email_address

            sender_address = "Example.com Support <support@example.com>"  #change  VVVVVVVVVVV
            subject = "Confirm your registration"
            body = """
                        Thank you for creating an account! Please confirm your email address by
                        clicking on the link below:
                        """  # %s then, confirmation_url

            mail.send_mail(sender_address, user_email_address, subject, body)

        else:
            print(" bad email ")   # bad email return

        #joscontactmessage.put()

    return render_to_response('contactus.html', template_values)
