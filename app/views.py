from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail

import os 


content = (
    {"des":"it's simple recipe app , you can add recipes , search recipes ,etc ...",
    "name":"recipe app","img":"main_background.jpeg",},

    {"des":"it's simple photo app ,you can download images , also upload to this app",
    "name":"photo app","img":"main_background.jpeg",},

    {"des":"it's simple todo app , you can add recipes , search recipes ,etc ...",
    "name":"to do app","img":"/home/shamsucm/Desktop/pc/python_django/my_projects/second_level/My_Portfolio/media/images/contact_background.jpeg",},

    {"des":"it's simple recipe app , you can add recipes , search recipes ,etc ...",
    "name":"recipe app","img":"app/main_background.jpeg",},

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

        send_mail(
            "message from"+email ,
            "hey i am"+name,
            message,
            ["shamsudheenchoyimadathil@gmail.com"],
            fail_silently=False,
        )

        return render(request,"main.html") 
    
        
    context["details_of_works"] = content

    return render(request,"main.html",context)
    