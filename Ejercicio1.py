
numCasos = int(input('Ingrese N: '))
while numCasos > 0:
    dif, ahorro = 0 , 0
    dias, semana = 0, 0
    x = float(input('Ingrese x: '))
    y = float(input('Ingrese y: '))
    a = float(input('Ingrese A: '))
    b = float(input('Ingrese B: '))
    
    dif = x - y
    ahorro = ahorro + b

    if dif > 0:
        while ahorro < a:
            ahorro = ahorro + (dif * 2)
            dias = dias + 1 
            if dias == 5:
                semana = semana + 1
                dias = 0
        print(semana,'SEMANAS',dias,'DIAS')
    else: 
        print('NO SE RECUPERA')
    numCasos = numCasos - 1
    pass

#Hagi Argani Mamani

