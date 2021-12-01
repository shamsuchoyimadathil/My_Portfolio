from django.shortcuts import  render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

import os 


content = (
    {"des":"it's food recipe app , collection of recipes , you can add,favourite,search them",
    "name":"recipe app","img":"media/food_recipe.png", "site":"https://chakkatherecipemanager.herokuapp.com/" ,
    "git":"https://github.com/shamsuchoyimadathil/food_recipes_app"},

    {"des":"collection of hd images, you can download them . also add to photopot",
    "name":"Photopot","img":"media/Photopot.png", "site":"https://photopot.herokuapp.com/" ,
    "git":"https://github.com/shamsuchoyimadathil/photopot_django"},

    {"des":"this site make you strong password with your instructions",
    "name":"password generator","img":"media/password_generator.png", "site":"https://strongpasswordgenerator.herokuapp.com/" ,
    "git":"https://github.com/shamsuchoyimadathil/Password-Generator-With-Django"},

    {"des":"it's my codepen link. in this page i did some styling with css",
    "name":"Frosted Glass","img":"media/Frosted_glass.png", "site":"https://codepen.io/shamsucm/pen/rNGawyN" ,
    "git":"https://github.com/shamsuchoyimadathil/frosted_glass_css"},

)


def main(request):
    context = {}

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message'] 

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