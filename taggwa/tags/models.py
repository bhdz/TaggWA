from django.db import models
from taggwa.common.models import RegisteredType
from taggwa.resources.models import Resource

# Create your models here.

class Tag(RegisteredType):
    """ Tags. base class """
    the_keyword = models.CharField(default = "", null = True)
    the_resource = models.ForeignKey(Resource)
    # Put a (tag, tag) relationship later... not needed
    