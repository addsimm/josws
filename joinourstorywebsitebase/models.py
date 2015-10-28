
from google.appengine.ext import ndb

# Create your models here.

def JOSUserSSS_key():
    """Constructs a Datastore key for the JOSContactMessage entity named JOSContactMessagesss."""
    return ndb.Key('JOSContactMessageSSS', 'JOSContactMessageSSS')

class JOSUser(ndb.Model):
    ju_first_name = ndb.StringProperty()
    ju_last_name = ndb.StringProperty()
    ju_messages = ndb.TextProperty(repeated=True)
    ju_date_created = ndb.DateTimeProperty(auto_now_add = True)

