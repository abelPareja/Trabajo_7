


"""Escribir una función que divida una cadena dada en una
lista de subcadenas cada vez que aparezca un carácter
específico."""


def palindromo():
    cadenaP = ''
    cadena2 = ''
    cadena = str(input("ingrese el nombre de la cadena"))
    valor = str(input("ingrse el separador"))

    for i in cadena:
        if(i ==valor):
            cadena2 = cadena2 + ' '
        else:
            cadena2 = cadena2 +i
            
        
    return cadena2    


a = palindromo()
print(a)
