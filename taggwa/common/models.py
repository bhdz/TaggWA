#from django.db import models

# Inherit your models from this one
class RegisteredType:
    """ This would represent a classes with ids.
    Inherit this class and add a call to [your class].register_class in your module.
    uppon module import the RegisteredType._reg dict would be filled with necesary i
    """
    _reg = {
        'classes' : { 'classid_key' : 'type'}, # forward search 
        'autoid' : -1, 
        'classids' : { 'type' : 'the_classid'}, # reversed search
    }
    
    the_classid = models.IntegerField(default = -1)  
    
    @classmethod
    def register_root(cls):
        """ this would register a base class hierarchy. call this only once each time in the form of
            BaseFoo.register_root()
        """
        if RegisteredType._reg['root_class'] is None:

            del RegisteredType._reg
            RegisteredType._reg = {
                'classes' : { 'classid_key' : 'type'},
                'autoid' : 0,
                'classids' : { 'type' : 'classid_key' },
            }
        RegisteredType._reg['root_class'] = cls 
        cls.register_class()
        
    @classmethod
    def register_class(cls):
        """ Register a type into the _reg"""
        if cls is RegisteredType:
            raise "Please do _not_ register RegisteredType!"
            
        cid = RegisteredType._reg[autoid]
        RegisteredType._reg['classes'][cls] = cid
        RegisteredType._reg['classids'][cid] = cls
        RegisteredType._reg['autoid'] += 1
        
    def upclass(self):
        """ this would return a properly instantiated model class from a 
            RegisteredType based subclass (i.e. a given Resource class)
            
            Each resource based class could be loaded from the database and
            upclassed into a proper class (inheritance from database classes)"""
        # I assume that self has been loaded properly from the database
        klass = RegisteredType._reg['classes'][self.the_classid]
        
        obj = klass.objects.get(pk = self.pk) 
        return obj # Ta-ta! 
        
    def get_classid(self):
        return RegisteredType['classids'][self.__class__]
    
    def __unicode__(self):
        print "@%s: the_type=%s;" % (id(self), self.the_classid)
    
    class Meta:
        abstract = True

class UniqueType(RegisteredType):
    """ tags are unique resources """
    pass 

class AmbiguousType(RegisteredType):
    """ Bookmarks are ambiguous types. """
    pass
