from django.test import TestCase
import math
# Create your tests here.

from functools import reduce
def calculeaza_factorial_v3(n):
    return  1 if n <2 else reduce(lambda x,y : x*y ,range(1,n+1))

def your_n(n):
    lista_factorial=[]
    for number in range(n,-1,-1):
        x=math.factorial(number)
        print(math.factorial(number))
        lista_factorial.append(x)
        
your_n(7)