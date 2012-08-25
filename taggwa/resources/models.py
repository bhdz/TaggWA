import urllib2

from django.db import models
from taggwa.common.models import *
from taggwa.tags.models import Tag

# Create your models here.

# murkyw:
# Each resource can be tagged with a keyword... Bookmarks are different 
#  beasts. (they are associated w/ a webuser)
#  Resources that are associated w/ tag but don't have Bookmarks entanglement
#   Are free to be claimed by users:
class Resource(RegisteredType):
    #the_tag = models.ForeignKey(Tag)
    pass

class Uri(Resource):
    the_url = models.CharField(default = "http://", max_length = 2048)
    
    def proto(self):
        """please return the protocol, see urllib2. Check for stale 
        links. etc."""
        pass
        
    def hostname(self):
        """return the hostname"""
        pass
    
    def __unicode__(self):
        pass
    
class UriNote(Uri):
    """ A note/URI association """
    the_note = models.CharField(default = "n/a", max_length = 4096)

#class Text(
#    """ leave a small textual notes  as resources."""