from django.shortcuts import render

# Create your views here.
def tabla_inmultirrii(request,num):
    num=int(num)
    valoare=[]
    for i in range(1,10):
      inmultire=i*num
      valoare.append(inmultire)
    context={
        'num':num,
        'inmultire':inmultire,
        'valoare':valoare,
    }
    return render(request,'Factorial.html',context)

