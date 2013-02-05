from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
import random
from dajax.core import Dajax

@dajaxice_register
def sayhello(request):
    return simplejson.dumps({'message':'Hello World'})



@dajaxice_register
def randomize(request):
    dajax = Dajax()
    dajax.assign('#result', 'value', random.randint(1, 10))
    return dajax.json()