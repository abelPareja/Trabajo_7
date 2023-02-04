
##############
import turtle

miTortuga = turtle.Turtle()
miVentana = turtle.Screen()

def dibujarEspiral(miTortuga, longitudLinea):
    while longitudLinea > 0:
        miTortuga.forward(longitudLinea)
        miTortuga.right(90)
        longitudLinea -=2

dibujarEspiral(miTortuga,100)
miVentana.exitonclick()
###########

import turtle

miTortuga = turtle.Turtle()
miVentana = turtle.Screen()

def dibujarEspiral(miTortuga, longitudLinea):
    if longitudLinea > 0:
        miTortuga.forward(longitudLinea)
        miTortuga.right(90)
        dibujarEspiral(miTortuga,longitudLinea-5)

dibujarEspiral(miTortuga,100)
miVentana.exitonclick()