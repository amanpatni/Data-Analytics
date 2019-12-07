from django.shortcuts import render

from .models import Jobs
# Create your views here.


def home(request):
    # we get the complete list of Jobs from DB
    job = Jobs.objects
    # now we are passing the jobs object to a dictionary
    return render(request, 'jobs\home.html', {'jobs': job})
