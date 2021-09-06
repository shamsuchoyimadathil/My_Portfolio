from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# class Main_page(TemplateView):

#     template_name = "main.html"

def main(request):

    return render(request,"main.html")
