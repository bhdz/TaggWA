from django.db import models
from taggwa.common.models import RegisteredType
# Create your models here.

class Tag(RegisteredType):
    """ Tags. base class """
    the_keyword = models.CharField(default = "", null = True)
    
    # Put a (tag, tag) relationship later... not needed
    