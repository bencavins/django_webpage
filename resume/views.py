from django.http import HttpResponse

from resume.models import Resume

def index(request):
    
    # Grab the resume created last
    resume = Resume.objects.order_by('-create_datetime')[0]
    output = 'This resume is for: '+resume.get_full_name()
    return HttpResponse(output)
