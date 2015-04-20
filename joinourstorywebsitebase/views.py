# Create your views here.
from __future__ import print_function

from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.core.validators import validate_email

from google.appengine.api import users
from google.appengine.api import mail

from joinourstorywebsitebase.models import *


def index(request):
   template_values = {}
   template_values.update({'page_name': 'Landing Page'
                           })

   return render_to_response('index.html', template_values)


def contactus(request):
    template_values = {}
    template_values.update(csrf(request))
    template_values.update({'page_name': 'Contact Us',
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

        user_email_address = request.POST['emailfield']
        print("joscontactemail:", user_email_address)          ### Logging

        try:                                                   # Confimation and email message to send
            validate_email(user_email_address)
            joscontactmessage.jcnm_email_address = user_email_address

            sender_address = "Join Our Story <info@joinourstory.com>"
            subject = "Your Recent Message"
            body = "Hi {0}, We received your message! We will do our best to respond quickly - hopefully within 24 hours. Thank you, Adam --- Message: {1}".format(

                joscontactmessage.jcm_first_name, joscontactmessage.jcm_message)

            mail.send_mail(sender_address, user_email_address, subject, body)           ### Reformat Body
            mail.send_mail("adam@joinourstory.com", user_email_address, subject, body)  ### Reformat Body
            template_values.update({'return_address': user_email_address,
                                    'return_message_flag': 1,
                                    'return_message': 'Email sent! If a confirmation email does not arrive soon, please try again or find help.'
                                    })
            joscontactmessage.put()
        except:                                                                         # Validation Fail
            template_values.update({'return_address': user_email_address,
                                    'return_message_flag': 1,
                                    'return_message': 'Email failed to send! Please try again or find help.'
                                    })

        return render_to_response('contactmessageresponse.html', template_values)


    return render_to_response('contactus.html', template_values)
