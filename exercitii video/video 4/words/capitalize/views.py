from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def capitalize_word(request,text):
    n=str(text)
    return HttpResponse(f'Aici este cuvantul tau capitalizat {text.upper()}')

def parametri_view(requests):
    print(requests.GET)
    primit = requests.GET.get('text')
    print('Ai primit',primit)
    if primit:
        return HttpResponse(primit.upper())
    else:
        return HttpResponse('Nu am primit un parametru text')