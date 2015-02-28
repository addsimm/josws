
from google.appengine.ext import ndb

# Create your models here.

def JOSContactMessageSSS_key():
    """Constructs a Datastore key for the JOSContactMessage entity named JOSContactMessagesss."""
    return ndb.Key('JOSContactMessageSSS', 'JOSContactMessageSSS')

class JOSContactMessage(ndb.Model):
    jcm_sender = ndb.UserProperty()
    jcm_first_name = ndb.StringProperty()
    jcm_last_name = ndb.StringProperty()
    jcm_email_address = ndb.StringProperty()
    jcm_message = ndb.TextProperty()
    jcm_date_created = ndb.DateTimeProperty(auto_now_add = True)

