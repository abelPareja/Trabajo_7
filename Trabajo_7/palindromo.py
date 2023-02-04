


"""Escribir una función que determine si una cadena es un
palíndromo (se lee igual en ambos sentidos) o no:"""




def palindromo():
    cadena2 = ''
    cadena = str(input("ingrese el nombre de la cadena"))
    for i in cadena:
        cadena2=  i + cadena2
    if (cadena == cadena2):
        print("La cadena introducida si corresponde a un palindromo")
    else:
        print("La cadena no es un palindromo")
    

palindromo()
