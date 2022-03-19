from itertools import count
listaNumeros=[]

longitud=int(input("Digite la cantidad de numeros que desea ingresar: "))
cout1=0
cout2=0
for i in range(longitud):
    numeroIngresado=int(input("ingrese un numero: "))
    if(numeroIngresado % 2==0):
        cout1=cout1+1

    if(numeroIngresado % 3==0):
        cout2=cout2+1

print(f'hay {cout1} multiplos de 2')
print(f'hay {cout2} multiplos de 3')