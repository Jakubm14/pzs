import  math, random, json, time

# Wczytanie pliku posortowanego
Plik_in = 'Lista_list.txt'
plik1=open(Plik_in)
abc = plik1.read ()
zest = json.loads (abc)

plik1.close()

wykaz = {}
# klucz - imię
# wartość: miasto, rok urodzenia, stawka

for linia in zest:
    wykaz [linia [0]] = [linia [1], linia [2], linia [3]]

miast = 'Kraków'
t0 = time.time ()
licz = 0
sred = 0
for klucz in wykaz:
    if wykaz [klucz][0] == miast:
        sred += wykaz [klucz][2]
        licz += 1
sred = sred / licz
      
t1 = time.time()
print (t1 - t0)
print ('Dla miasta ',miast,' średnie wynagrodzenie =',sred)

miasto = {}
def init_rev (wykaz, miasto): #funkcja inicjuje słownik 'odwrotny'
    for poz in wykaz:
        war = wykaz [poz][0] in miasto.keys()
        if war == False:
            miasto [wykaz[poz][0]] = []
    return miasto

def creat_rev (wykaz, miasto):
    for poz in wykaz:
        miasto [wykaz [poz][0]].append([poz, wykaz [poz][1], wykaz [poz][2]])
    return miasto
init_rev (wykaz, miasto)

miasto = creat_rev (wykaz, miasto)

miast = 'Kraków'
t0 = time.time ()
licz = 0
sred = 0
for elem in miasto[miast]:
        sred += elem[2]
        licz += 1
sred = sred / licz
      
t1 = time.time()
print (t1 - t0)
print ('Dla miasta ',miast,' średnie wynagrodzenie =',sred)
