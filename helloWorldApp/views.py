# -*- coding: utf-8 -*-
from django.http import HttpResponse

def index(request):
    return HttpResponse("I did it. Hello world App")