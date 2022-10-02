# Autor: Chocolatin
# Metodos Numericos
# --CREACION DE LA FUNCION SOBRE METODO DEL PUNTO FIJO PARA LLAMARLO EN CADA F(X)

import numpy as np
def puntofijo(x):  # x es el valor de prueba para las funciones ej  x= 0.5
  i=0
  funcion = 100      #Valor de prueba para primer iteracion en la resta del error
  Eencontrado = True
  while Eencontrado == True:
    funanterior = f(x)
    xi = g(x)
    error = funcion-funanterior
    abss = np.abs(error)
    funcion = f(x)
    x = xi
    Eencontrado = abss > 0.019 
    funanterior = funcion
    i += 1
  print(f"Iteracion: {i} \n\txi ={x}\tf(x)= {funcion}\tError= {abss}") 
  print("\t_______________________________________________________________________")
  
  
  
##  
 
################################## EJEMPLOO de uso ##########################################################

#Funcion x
def f(x):
  return  x**6- 1.2999059*x**5- 26.86516*x**4+ 9.31798*x**3 + 145.75786*x**2 + 79.99707*x - 0.16472  #Funcion Original 
#Funccion g
def g(x):
  return  (1.2999059*x**5 + 26.86516*x**4 - 9.31798*x**3 - 145.75786*x**2 - 79.99707*x + 0.16472)**(1/6)

# LLAMADA AL METODO PUNTO FIJO
puntofijo(5)  #valor x probado x =5
# Nos imprime el resultado


################################# Division con el valor obtenido ###########################################
#Funcion Division de polinomios
import sympy
def divison(P2):
    #Definimos los simbolos con la funcion symbols de sympy
    sympy.init_printing()
    x,y = sympy.symbols('x,y')
    P1 = f(x)  #Funcion en donde estamos resolviendo el punto fijo
    d1 = sympy.Poly(P1)
    d2 = sympy.Poly(P2)
    def div(p1, p2):
        return p1 // p2
    print("Division: \n", div(d1, d2))
 

### LLAMAMOS AL METODO DIVISION
divison(x-5.0055)  #x-5.005 es el resultado de xi en el metodo del punto fijo xi = 5.005  ->   x - 5.005(para su division)
                   # Si el resultado saldria negativo xi = -5.005  entonces -> x + 5.005(para su division)

# Nos imprime el resultado





