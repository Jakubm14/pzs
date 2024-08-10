#from math import *
import time, math
def funkcja (x): 
    wart = x**2 - x + 1
    return wart

def pole (a, b, n):
    delta = (b - a)/n
    suma = 0
    val = a
    while val < b:
        suma = suma + (funkcja(val) + funkcja(val + delta))*delta / 2
        val = val + delta       
    return suma
def calka (a, b, epsilon):
    roznica = 1
    n = 1
    val_1 = pole (a, b, n)
    licznik = 0
    while roznica > epsilon:
        licznik = licznik + 1
        n = n * 2
        val_2 = pole (a, b, n)
        roznica = math.fabs ((val_2 - val_1)/val_2)
        val_1 = val_2
    return val_2, n, licznik
dol_gr = 0
gor_gr = 10
epsilon = 10**-12
t0=time.time()
integral, n, licznik = calka (dol_gr, gor_gr, epsilon)
t1=time.time()
print ('Wartość całki oznaczonej w przedziale od ',dol_gr,'do ',gor_gr,'  ',integral,'\n','Przedział podzielony na ',n,' odcinków\n','Liczba iteracji = ',licznik)
print (t1 - t0)



