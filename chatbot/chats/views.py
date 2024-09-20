from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest


def main_page(request: HttpRequest):
    return HttpResponse("This is where you can chat with my chatbots.")
