# Create your views here.
from __future__ import print_function

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext

from django.core.context_processors import csrf


from django.core.validators import validate_email

from google.appengine.api import users
from google.appengine.api import mail   # --enable_

from joinourstorywebsitebase.models import *


def tempindex(request):
   template_values = {}
   current_user = ''  ##### find current user
   context = RequestContext(request, template_values)
   context.update({'page_name': 'Landing Page',
                   'user': current_user
                   })

   return render_to_response('tempindex.html', context)

def index(request):
   template_values = {}
   current_user = ''  ##### find current user
   context = RequestContext(request, template_values)
   context.update({'page_name': 'Landing Page',
                   'user': current_user
                   })

   return render_to_response('index.html', context)


def contactus(request):
    context = {}
    context.update(csrf(request))
    context.update({'page_name': 'Contact Us',
                            'return_message_flag': 0,
                            'return_message': ' '
                            })

    if request.method == 'POST':
        ### FOR DEBUG raise KeyError(request.POST)
        joscontactmessage = JOSContactMessage(parent = JOSContactMessageSSS_key())  # Message instance

        if users.get_current_user():
            joscontactmessage.jcm_sender = users.get_current_user()

        joscontactmessage.jcm_first_name = request.POST['firstnamefield']
        joscontactmessage.jcm_last_name = request.POST['lastnamefield']
        joscontactmessage.jcm_message = request.POST['messagefield']

        sender_address = "Adam S. <adam@joinourstory.com>" # must be google apps admin

        user_email_address = request.POST['emailfield']
        print("joscontactemail:", user_email_address)          ### Logging

        try:                                                   # Confimation and email message to send
            validate_email(user_email_address)
            joscontactmessage.jcm_email_address = user_email_address


            subject = "Your Recent Message"
            body = "Hi {0}, We received your message! We will do our best to respond quickly - hopefully within 24 hours. Thank you, Adam --- Message: {1}".format(

                joscontactmessage.jcm_first_name, joscontactmessage.jcm_message)

            mail.send_mail(sender_address, user_email_address, subject, body)  ### Reformat Body
            mail.send_mail(sender_address, "info@joinourstory.com", subject + " " + user_email_address, body)  ### Reformat Body
            context.update({'return_address': user_email_address,
                                    'return_message_flag': 1,
                                    'return_message': 'Email sent! If a confirmation email does not arrive soon, please try again or find help.'
                                    })
            joscontactmessage.put()

        except:                                                  # Validation Fail

            context.update({'return_address': user_email_address,
                                    'return_message_flag': 1,
                                    'return_message': 'Email failed to send! Please try again or find help.'
                                    })

        return render_to_response('contactmessageresponse.html', context)


    return render_to_response('contactus.html', context)
