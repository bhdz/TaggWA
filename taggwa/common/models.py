from django.db import models

# Create your models here.
class RegisteredType:
    """ All Resource types must be registered here on model import.
    One _reg to Rule them types all :]
    """
    _reg = {
        'classes' : { 'classid_key' : 'type'}, # forward search ("Give me a class by classid")
        'autoid' : -1, # When this thing becomes mime, update autoid to 
        'classids' : { 'type' : 'the_classid'}, # reversed search ("Give me a classid by type")
        'root_class' : None, # register this
    }
    
    # Each registered model has classid here BUT!
    #  ...this could be "upgraded" to mime_types in the future one integer (two 
    #  ... hashes for "type/subtype" because it is nicer and fancier methods 
    #  could be used for updating the SQL database)
    the_classid = models.IntegerField(default = -1)  
    
    @classmethod
    def register_root(cls):
        """ this would register a base class hierarchy. call this only once each time in the form of
            BaseFoo.register_root()
        """
        if RegisteredType._reg['root_class'] is None:
            # remove all registered classes in one sweep
            del RegisteredType._reg
            RegisteredType._reg = {
                'classes' : { 'classid_key' : 'type'}, # forward search ("Give me a class by a primary key")
                'autoid' : 0, # each time ... do i really need this?
                'classids' : { 'type' : 'classid_key' }, # reversed search ("Give me a primary key from a class")
                'root_class' : None,
            }
        RegisteredType._reg['root_class'] = cls # not used at the moment
        cls.register_class()
        
    @classmethod
    def register_class(cls):
        """ Register a type into the _reg"""
        if cls is RegisteredType:
            raise "Please do _not_ register RegisteredType!" # Kiss
            
        cid = RegisteredType._reg[autoid]
        RegisteredType._reg['classes'][cls] = cid
        RegisteredType._reg['classids'][cid] = cls
        RegisteredType._reg['autoid'] += 1
        
    def upclass(self):
        """ this would return a properly instantiated model class from a 
            RegisteredType based subclass (i.e. a given Resource class)
            
            Each resource based class could be loaded from the database and
            upclassed into a proper class (inheritance from database classes"""
        # I assume that self has been loaded properly from the database
        klass = RegisteredType._reg['classes'][self.the_classid]
        # Now, upclassing is just select()ing another table.
        
        # Magic mantra. 
        #   All derivatives 
        #   of RegisteredType share primary key w/ this one, because 
        #   they are declared abstract.
        obj = klass.objects.get(pk = self.pk) 
        return obj # Ta-ta! 
        
    def get_classid(self):
        return RegisteredType['classids'][self.__class__]
    
    def __unicode__(self):
        print "@%s: the_type=%s;" % (id(self), self.the_classid)
    
    class Meta:
        abstract = True # Has to be a model i guess. Each class must hold classids in it's own table

# Murkyw (boril):
# Todo: Add base differentiation between UniqueResources and 
# Non-unique resources
#
# Tags are unique types (mark them into the database with Meta class, if django 
#    supports it) 
# Resources are unique too
# But Bookmarks (grouping w/ a concrete WebUser in mind is not is not)
# Somehow, the descendents of UniqueType must "enforce" unique.
#  __init__? __new__?
class UniqueType(RegisteredType):
    pass 

class AmbiguousType(RegisteredType):
    pass
