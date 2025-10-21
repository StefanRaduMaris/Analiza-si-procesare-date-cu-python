from django.shortcuts import render
from django.http import HttpResponse
import random
import string
import pandas as pd


# Create your views here.

CIFRE=[str(i) for i in range(10)]
LITERE_MARI=[chr(i) for i in range(ord('A'),ord('Z')+1)] 
LITERE_MICI=[chr(i) for i in range(ord('a'),ord('z')+1)] 
TOT=CIFRE+LITERE_MARI+LITERE_MICI



def alege_view(requests):

    
    Options=string.ascii_lowercase 
    if requests.GET.get('whithupper'):
        Option  += string.ascii_uppercase 
    if requests.GET.get('whithdigits'):
        Options += string.digits  
    if requests.GET.get('whithpunctuation'):
        Option += string.punctuation

    print(requests.GET)
    context={
    }
    lungime=requests.GET.get('lungime')
    print(lungime)
    lungime = int(lungime)
    try:
        if lungime:
            parola ="" 
            for i in range(lungime):
                parola += random.choice(Options)
            context['parola'] = parola

        df = pd.read_csv('parole.csv')
        df.loc[len(df)]==parola
        df.to_csv('parole.csv')
    except:
        pass

    return render(requests,'alege.html',context)