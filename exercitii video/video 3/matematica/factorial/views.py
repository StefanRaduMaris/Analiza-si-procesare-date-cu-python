from django.shortcuts import render
import math
from django.http import HttpResponse
from functools import reduce

# Create your views here.
def factorial_view(requests,n):
    try:
        n=int(n)
    except:
        return HttpResponse("Nu se poate calcula")  
    if n<0:
        return HttpResponse(f'Numarul {n} trebuie sa fie mai mare ca 0')
    else:
        return HttpResponse(f'''Numarul {n} are factorialul {math.factorial(n)}''')

def calculeaza_factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * calculeaza_factorial(n-1)

def factorial_template_view(request,n):
    n=int(n)
    lista_factorial=[]
    for number in range(n,-1,-1):
        x=math.factorial(number)
        print(math.factorial(number))
        lista_factorial.append(x)

    produs = 1 if n < 2 else reduce(lambda x,y : x*y ,range(1,n+1))
    context={
        'n':n,
        'produs':produs,
        'lista':lista_factorial
    }
    return render(request,'factorial.html',context)