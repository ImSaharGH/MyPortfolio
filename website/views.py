from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def home_view(request):
    return render(request, 'website/dark.html')



