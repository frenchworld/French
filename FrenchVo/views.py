from django.shortcuts import render

from FrenchVo.models import French, Verbir, Verber, Verbre


def index(request):
    debts = French.objects.all()



    return render(request, "index.html", {'debts': debts})

def phrase(request):
    return render(request, "phrase.html")

def home(request):
    return render(request, "home.html")

def erending(request):
    debter = Verber.objects.all()
    return render(request, "er.html", {'debter': debter})
def reending(request):
    debtre= Verbre.objects.all()
    return render(request, "re.html", {'debtre': debtre})
def irending(request):
    debtir= Verbir.objects.all()
    return render(request, "ir.html", {'debtir': debtir})