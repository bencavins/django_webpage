from django.http import HttpResponse
from django.shortcuts import render

from resume.models import Resume

def index(request):
    
    # Grab the resume created last
    resume = Resume.objects.order_by('-create_datetime')[0]
    context = {'resume': resume}
    return render(request, 'resume/index.html', context)
