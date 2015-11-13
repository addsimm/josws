# Create your views here.
from __future__ import print_function

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext

from django.core.context_processors import csrf

from django.core.validators import validate_email

from google.appengine.api import users
from google.appengine.api import mail   # --enable_

from joinourstorywebsitebase.models import *

import six


def landingpage(request):
   template_values = {}
   context = RequestContext(request, template_values)
   context.update({'page_name': 'Landing Page'
                   })

   return render_to_response('landingpage.html', context)

def index(request):
   template_values = {}
   context = RequestContext(request, template_values)
   context.update({'page_name': 'Home'
                   })

   if request.method == 'POST':
        user_email_address = request.POST['emailfield']
        # print("JOS User Email Address:", user_email_address)    ### Logging

        josuser = JOSUser.get_or_insert(user_email_address)

        messages = josuser.ju_messages
        messages.insert(0, "newsletter subscription")
        josuser.ju_messages = messages

        sender_address = "Joinus <joinus@joinourstory.com>" # must be google apps admin
        subject = "Succesfully Subcribed to Hollywood Heights Updates"
        body = "Thank you for your interest in Hollywood Heights! Please stay tuned for news and updates. If you do not receive our emails, check your spam folder and/or add adam@joinourstory.com to your contact list"

        # print("Contact Message Body:", body)
        mail.send_mail(sender_address, user_email_address, subject, body)
        mail.send_mail(sender_address, "info@joinourstory.com", subject + "; " + user_email_address, body)
        context.update({'return_address': user_email_address,
                        'return_message_flag': 1,
                        'return_message': 'Subscription succssful! If a confirmation does not arrive soon, please check the address you gave and try again.'})
        # print("Message Saving")
        josuser.put()

        return render_to_response('contactmessageresponse.html', context)

   return render_to_response('index.html', context)


def contactus(request):
    template_values = {}
    context = RequestContext(request, template_values)
    context.update(csrf(request))
    context.update({'page_name': 'Contact Us',
                    'return_message_flag': 0,
                    'return_message': ' '
                    })

    if request.method == 'POST':
        user_email_address = request.POST['emailfield']
        # print("JOS User Email Address:", user_email_address)    ### Logging

        josuser = JOSUser.get_or_insert(user_email_address)

        josuser.ju_first_name = request.POST['firstnamefield']
        if isinstance(request.POST['lastnamefield'], six.string_types):
            josuser.ju_last_name = request.POST['lastnamefield']
        elif isinstance(josuser.ju_last_name, six.string_types):
            pass
        else:
            josuser.ju_last_name = 'x'

        this_message = request.POST['messagefield']
        user_messages = josuser.ju_messages
        user_messages.insert(0, this_message)

        sender_address = "Joinus <joinus@joinourstory.com>" # must be google apps admin
        subject1 = "Your Recent Message to JOS"
        body = "Hi {0}, We received your message! We will do our best to respond quickly - hopefully,  within 24 hours. Thank you! --- Message: {1}".format(josuser.ju_first_name, this_message)

        # print("Contact Message Body:", body)
        mail.send_mail(sender_address, user_email_address, subject1, body)
        mail.send_mail(sender_address, "info@joinourstory.com", subject1 + "; " + user_email_address, body)
        context.update({'return_address': user_email_address,
                        'return_message_flag': 1,
                        'return_message': 'Message sent. If a confirmation does not arrive soon, please check the address you gave and try again.'})
        # print("Message Saving")
        josuser.put()

        return render_to_response('contactmessageresponse.html', context)

    return render_to_response('contactus.html', context)


