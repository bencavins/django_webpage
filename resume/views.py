from django.http import HttpResponse
from django.shortcuts import render

from resume.models import Resume

def index(request):
    
    # Grab the resume created last
    resume_list = Resume.objects.order_by('-create_datetime')
    resume = resume_list[0] if resume_list else None
    context = {'resume': resume}
    return render(request, 'resume/index.html', context)
