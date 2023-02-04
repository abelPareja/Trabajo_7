

"""Escribir una función que determine la longitud de la
subcadena más larga que no contiene ninguna letra
repetida."""



def palindromo():
    cadenaP = ''
    cadena2 = ''
    cadena = str(input("ingrese el nombre de la cadena"))
    

        
    for i in cadena:
        if(i ==' '):
            if(sinRep(cadena2) == 1):
                cadenaP = cadenaP  + cadena2
            cadena2 = ''
        else:
            cadena2  = cadena2 + i  
    return cadenaP     
    
def sinRep(cadena):
    c = 0
    for i in cadena:
        for j in cadena:
            if(i == j):
                c = c+1
    if (c == len(cadena) ):
        c = 1
    return c
                           
for i in palindromo():
    print(i)
    

    
