#dy/dx = f(x,y) con intervalo [0,4] con y(0) = PI
import matplotlib.pyplot as plt # Se llama la libreria para poder graficar
import numpy as np              # Se llama la libreria para operaciones matematicas

def f(x,y):               # Se define la funcion dada
  return y * np.cos(x)**2

def Runge_kutta_1(f,a,b,h,y0):      # Se define la funcion para Runge_Kutta 1er grado

  x = [a]                         # Se toma el valor de x como una lista en a de la funcion
  y = [y0]                        # Se toma el valor de yo como valor inicial
  while x[-1]< b:                 # Se abre el ciclo while
    y.append(y[-1] + f(x[-1], y[-1]) *h)   # Se adiciona los valores a la lista de y
    x.append(x[-1] + h)                    # Se gusrdan los valores a la lista de x
  return x,y

def Runge_kutta_2(f,a,b,h,y0):       # Se define la funcion para Runge_Kutta 2do grado
  x = [a]
  y = [y0]
  while x[-1]< b:
      k1 = f(x[-1], y[-1])
      k2 = f(x[-1] +  3/4 * h, y[-1]+ 3/4 * k1 *h)
      y.append(y[-1] + (1/3 * k1 + 2/3 * k2) * h)
      x.append(x[-1] + h)
  return x,y

def Runge_kutta_4(f,a,b,h,y0):         # Se define la funcion para Runge_Kutta 4to grado
  x = [a]
  y = [y0]
  while x[-1]< b:
      k1 = f(x[-1], y[-1])
      k2 = f(x[-1] +  0.5 * h, y[-1]+ 0.5 * k1 *h)
      k3 = f(x[-1] +  0.5 * h, y[-1]+ 0.5 * k2 *h)
      k4 = f(x[-1]+ h , y[-1]+ k3 *h)
      y.append(y[-1] + (1/6) * k1 + 2 * k2 + 2 *k3 + k4)
      x.append(x[-1] + h)
  return x,y

h = 0.5      # Se referencia el valor de h con 0.5

print("Tamaño de paso h:", h) # Se imprime el valor de h
x1,y1 = Runge_kutta_1(f,0,4,h,np.pi)       # Se crean las variables para el grado 1 con x y y
x2,y2 = Runge_kutta_2(f,0,4,h,np.pi)      # Se crean las variables para el grado 2 con x y y
x4,y4 = Runge_kutta_4(f,0,4,h,np.pi)      # Se crean las variables para el grado 4 con x y y

print("Grado 1: ",x1,y1)
print("Grado 2: ",x2,y2)
print("Grado 4: ",x4,y4)


plt.figure(figsize=(16,10), dpi= 30)  # Se crea el display de la grafica
plt.plot(x1,y1 ,label= "Rk primer Grado", color="r")         # Se llama a graficar el grado 1, dandole un nombre y un color
plt.legend()                                # Se crea el titulo de la grafica
plt.grid()                                 # Se llama a dibujar las celdas
plt.show()                               #Se llama la funcion que muestra la grafica
plt.figure(figsize=(16,10), dpi= 30)
plt.plot(x2,y2 ,label= "Rk segundo Grado",color="orange")        # Se llama a graficar el grado 2, dandole un nombre y un color
plt.legend()
plt.grid()
plt.show()
plt.figure(figsize=(16,10), dpi= 30)
plt.plot(x4,y4 ,label= "Rk cuarto Grado",color="blue")        # Se llama a graficar el grado 4, dandole un nombre y un color
plt.legend()
plt.grid()
plt.show()

h = 0.1            # Se referencia el valor de h con 0.1

print("Tamaño de paso h:", h)
x1,y1 = Runge_kutta_1(f,0,4,h,np.pi)
x2,y2 = Runge_kutta_2(f,0,4,h,np.pi)
x4,y4 = Runge_kutta_4(f,0,4,h,np.pi)

print("Grado 1: ",x1,y1)
print("Grado 2: ",x2,y2)
print("Grado 4: ",x4,y4)

plt.figure(figsize=(16,10), dpi= 30)
plt.plot(x1,y1 ,label= "Rk primer Grado", color="r")
plt.legend()
plt.grid()
plt.show()
plt.figure(figsize=(16,10), dpi= 30)
plt.plot(x2,y2 ,label= "Rk segundo Grado",color="orange")
plt.legend()
plt.grid()
plt.show()
plt.figure(figsize=(16,10), dpi= 30)
plt.plot(x4,y4 ,label= "Rk cuarto Grado",color="blue")
plt.legend()
plt.grid()
plt.show()

h = 0.05         # Se referencia el valor de h con 0.05

print("Tamaño de paso h:", h)
x1,y1 = Runge_kutta_1(f,0,4,h,np.pi)
x2,y2 = Runge_kutta_2(f,0,4,h,np.pi)
x4,y4 = Runge_kutta_4(f,0,4,h,np.pi)

print("Grado 1: ",x1,y1)
print("Grado 2: ",x2,y2)
print("Grado 4: ",x4,y4)

plt.figure(figsize=(16,10), dpi= 30)
plt.plot(x1,y1 ,label= "Rk primer Grado", color="r")
plt.legend()
plt.grid()
plt.show()
plt.figure(figsize=(16,10), dpi= 30)
plt.plot(x2,y2 ,label= "Rk segundo Grado",color="orange")
plt.legend()
plt.grid()
plt.show()
plt.figure(figsize=(16,10), dpi= 30)
plt.plot(x4,y4 ,label= "Rk cuarto Grado",color="blue")
plt.legend()
plt.grid()
plt.show()