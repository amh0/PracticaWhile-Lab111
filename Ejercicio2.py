
a = int(input('Ingrese un numero: '))
if a >= 0:
    numaux = a
    cont = a
    num1 = a 
    while cont > 1:
        numaux = numaux - 1
        num2 = numaux 
        while num2 > 1:
            num1 = num1 + a
            num2 = num2 - 1
        a = num1
        cont = cont - 1
    print ('El factorial es:',num1)
else:
    print('El numero no es un numero natural.')

#Hagi Argani Mamani

