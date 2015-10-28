
from google.appengine.ext import ndb

# Create your models here.

class JOSUser(ndb.Model):
    ju_first_name = ndb.StringProperty(default='empty')
    ju_last_name = ndb.StringProperty(default='empty')
    ju_messages = ndb.TextProperty(repeated=True)
    ju_date_created = ndb.DateTimeProperty(auto_now_add = True)

