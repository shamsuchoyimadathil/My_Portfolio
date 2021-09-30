from abc import ABCMeta
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

import os 


content = (
    {"des":"it's simple photo app ,you can download images , also upload to this app",
    "name":"recipe app","img":"media/main_background.jpeg",},

    {"des":"it's simple todo app , you can add recipes , search recipes ,etc ...",
    "name":"recipe app","img":"media/main_background.jpeg",},

    {"des":"it's simple photo app ,you can download images , also upload to this app",
    "name":"recipe app","img":"media/main_background.jpeg",},

    {"des":"it's simple todo app , you can add recipes , search recipes ,etc ...",
    "name":"recipe app","img":"media/main_background.jpeg",},

    {"des":"it's simple photo app ,you can download images , also upload to this app",
    "name":"recipe app","img":"media/main_background.jpeg",},

    {"des":"it's simple todo app , you can add recipes , search recipes ,etc ...",
    "name":"recipe app","img":"media/main_background.jpeg",},
)


def main(request):
    context = {}

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message'] 

        if name == "" or email == "" or message == "":
            context["no_info"] = "please complete the fields"
            return render(request,"main.html",context)
        else:
            send_mail(
            "message from "+email ,
            message,
            "hey i am "+name,
            ["shamsudheenchoyimadathil@gmail.com"],
            fail_silently=False,
            )
            return HttpResponseRedirect(reverse('main'))

    context["details_of_works"] = content

    return render(request,"main.html",context)