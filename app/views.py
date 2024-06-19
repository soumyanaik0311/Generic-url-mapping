from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def srujana(request):
    return HttpResponse("<h1><marquee>hii, I am Srujana here</h1></marquee>")

def meghana(request):
    return HttpResponse("<h1><marquee>hii, I am Meghana Here</h1></marquee>")

