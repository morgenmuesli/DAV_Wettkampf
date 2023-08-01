from django.shortcuts import render
from .models import Member


# Create your views here.
def index(request):
    return render(request, 'index.html')


def post(request):
    return render(request, "post.html")


def team(request):
    trainer = Member.objects.filter(category="TR")
    athletes = Member.objects.filter(category="AT")
    context = {
        "trainers": trainer,
        "athletes": athletes
    }

    return render(request, 'team.html', context=context)
