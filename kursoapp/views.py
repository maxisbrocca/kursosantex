from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import HomePostForm, BlogPostForm, ClienteForm, RespuestaBlogPostForm, DiapositivaForm, ServicioForm
from models import HomePost

classnames = {'homepost': HomePostForm,
              'blogpost': BlogPostForm,
              'respuestablogpost': RespuestaBlogPostForm,
              'cliente': ClienteForm,
              'diapositiva': DiapositivaForm,
              'servicio': ServicioForm}

@login_required
def home(request):
    posts = HomePost.objects.filter(activo=True)
    d = {'parametro': "Hola mundo!", "posts": posts}
    return render_to_response('home.html', d, context_instance=RequestContext(request))



@login_required
def new(request, classname):
    if classname not in classnames.keys():
        return HttpResponseRedirect(reverse('home_view'))
    formclass = classnames.get(classname)
    if request.method == 'POST':
        form = formclass(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home_view'))
    else:
        form = formclass()
    return render_to_response('modelform.html', {'form': form},
        context_instance=RequestContext(request))