from django.http import HttpResponse
from django.template import Context, loader

from resume.models import Resume

def index(request):
    
    # Grab the resume created last
    resume = Resume.objects.order_by('-create_datetime')[0]
    template = loader.get_template('resume/index.html')
    context = Context({'resume': resume})
    return HttpResponse(template.render(context))
