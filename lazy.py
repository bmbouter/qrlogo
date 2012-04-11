# file lazy.py
from django.core import urlresolvers

class lazy_string(object):
    def __init__(self, function, *args, **kwargs):
        self.function=function
        self.args=args
        self.kwargs=kwargs
        
    def __str__(self):
        if not hasattr(self, 'str'):
            self.str=self.function(*self.args, **self.kwargs)
        return self.str

def reverse(*args, **kwargs):
    return lazy_string(urlresolvers.reverse, *args, **kwargs)
