from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def sample_view(request):
    context = RequestContext(request)
    video = {'url': 'http://www.youtube.com/watch?v=kFNaqX-dvPM'}
    return render_to_response('myapp/test_template.html', {'my_video': video }, context)