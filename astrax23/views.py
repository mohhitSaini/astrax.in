from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import (Speaker,Sponsor,Team)

def home(request):
    content ={
        'speakers_details':Speaker.objects.all(),
        'sponsors':Sponsor.objects.all(),
        'team_members':Team.objects.all(),
    }
    return render(request,'base.html',content)



