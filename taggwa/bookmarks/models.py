from django.db import models

from taggwa.common.models import *
from taggwa.webuser.models import WebUser
from taggwa.tags.models import Tag
from taggwa.resources.models import *

# Create your models here.
#  grouping things: groupings of tags, resources, and a concrete WebUser
class Bookmark(models.Model):
    """Main resource grouping"""
    # Primary key might include this one!
    the_webuser = models.ForeignKey(WebUser) # self.__class__ <-*--> WebUser
    the_tags = models.ManyToManyField(Tag) # self.__class__ <-*--> Tag
    the_resources = models.ManyToManyField(Resource)
    #class Meta:
    #    pass
