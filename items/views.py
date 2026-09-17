from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, items index.")

def detail_item(request, item_id):
    return HttpResponse("Seeing the item n. %s." % item_id)

