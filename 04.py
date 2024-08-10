import random
import time
licz = 0
plik = open ('imiona_losowe.txt')
lista01 = []

for poz in plik:
    lista01.append(poz[:-1])


plik.closed

print (lista01)
print ('Liczba imion = ',len (lista01))
input()

lista02 = lista01 [0:]

wsk = 0
while wsk == 0:

    wsk = 1
    for licz in range (0,  len (lista01)-1):
        if lista01 [licz + 1] < lista01 [licz]:
            wsk = 0
            lista01 [licz], lista01 [licz + 1] = lista01 [licz + 1], lista01 [licz]
print (lista01)

licz = 0
dzw = 1.3
k = len (lista01) -1
rzp = int (k / dzw)
i = 0
t0 = time.time()
while rzp >=1:
    i = 0 
    while i + rzp <=k:
        if lista01[i] > lista01[i+rzp]:
            s = lista01[i]
            lista01[i] = lista01[i+rzp]
            lista01[i+rzp] = s
            licz = licz + 1
        i=i+1
    rzp = int (rzp / dzw)
t1 = time.time()
print('Sortowanie grzebieniowe - czas: ', t1 - t0)
print('Lista posortowana:',lista01)
print ('Liczba zmian = ', licz)

t0 = time.time()
   
dlug = len (lista02)
wsk = 0
while wsk == 0:
    wsk = 1
    for licz2 in range (0, dlug -1):
        if lista02 [licz2] > lista02 [licz2 + 1]:
            wsk = 0
            lista02 [licz2], lista02 [licz2+1] = lista02 [licz2+1], lista02 [licz2]

  #  input()

t1 = time.time()
print (t1 - t0)
print (lista02)
print('Sortowanie bąbelkowe - czas: ', t1 - t0)
print('Lista posortowana:',lista02)




