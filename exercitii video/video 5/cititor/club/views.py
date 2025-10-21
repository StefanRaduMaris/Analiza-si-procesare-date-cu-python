from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def validare_cnp_view(requests):
    context={

    }
    return render(requests,'formular_cnp.html',context)

def valideaza_cnp(cnp:str):
    return True
    
def rezultat_cnp_view(requests):
    print(requests.POST)
    cnp=requests.POST.get('cnp')
    print('CNP-ul primit e : ',cnp)

    context={
        'valid':valideaza_cnp(cnp)
    }
    return render(requests,'rezultat_formular_cnp.html',context)