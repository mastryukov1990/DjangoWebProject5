from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {   'title' : "Hi",
            'message' : "hii, ",
            'content':" on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )


def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title' : "Trading",
            'content' : "Here, Nikita will share with you some ways to play."
        }
    )