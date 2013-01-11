from django.template import RequestContext
from django.shortcuts import *
from models import *

def home(request):
	data = Data.objects.get(id = 1)
	return render_to_response('home.html', locals(),
				  context_instance = RequestContext(request))