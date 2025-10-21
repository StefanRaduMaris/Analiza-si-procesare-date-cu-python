
import math
from functools import reduce

lista = [10,2,15,40,100,200]
culori = ['alb','rosu','galben','mov','portocaliu','albastru']
print(list(filter(lambda x : x > 5,lista)))
print(reduce(lambda x,y: x if len(x) < len(y) else y,culori))

print(list(filter(lambda x : x>101,lista)))
#filter lambda
print(list(filter(lambda x : x < 20,lista )))
#list comprehension
print([elem for elem in lista if elem > 5])

vocale='aeiouAEIOU'
input='Salut , ce mai faci?'

def elimina_vocale(ch):
    return ch not in vocale
#varianta 1 functie
print(''.join(filter(elimina_vocale,input)))
#varianta 2 lambda
print(''.join(filter(lambda x : x not in vocale , input)))
#varianta 3 list comprehension
print(''.join(ch for ch in input if ch not in vocale))


#realizeaza o lista cu stringuri intr-o linie de cod
my_list=list(range(1,5))
print(my_list)
#mapping
my_list=list(map(lambda x: str(x),range(1,5)))
print(my_list)
#list comprehension
my_list=[str(x) for x in range(0,5)]
print(my_list)

#avem o lista , facem o functie care returneaza media
lista_numere = [100,15,14,2,93,12]
print(sum(lista_numere)/len(lista_numere))
#versiunea 2
print(reduce(lambda x,y : x+y ,lista_numere)/len(lista_numere))
