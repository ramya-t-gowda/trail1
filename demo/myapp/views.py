from pyexpat.errors import messages
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from django.core.serializers import json
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import Context, loader
from django.db.models import Count, Q
from django.shortcuts import render
from django.urls import reverse

from .models import Motor
from django.shortcuts import render, get_object_or_404

def index(request):
    template = loader.get_template("./myapp/index.html")
    return HttpResponse(template.render())








def login(request):
    template = loader.get_template("./myapp/login.html")
    return HttpResponse(template.render())


def register(request):
    template = loader.get_template("./myapp/register.html")
    return HttpResponse(template.render())


def anomalies(request):
    template = loader.get_template("./myapp/anomalies.html")
    return HttpResponse(template.render())


def manuals(request):
    template = loader.get_template("./myapp/manuals.html")
    return HttpResponse(template.render())


def spareparts(request):
    template = loader.get_template("./myapp/spareparts.html")
    return HttpResponse(template.render())


def aboutus(request):
    template = loader.get_template("./myapp/aboutus.html")
    return HttpResponse(template.render())


def dashboard(request):
    template = loader.get_template("./myapp/dashboard.html")
    return HttpResponse(template.render())
