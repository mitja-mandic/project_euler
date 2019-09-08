#problem 11
datoteka = 'project_euler_11.txt'
with open(datoteka, 'r') as f:
    s = []
    for vrstica in f:
        s.append(vrstica)
novSez = []
for x in s:
    j = x.split(' ')
    k = [int(i) for i in j]
    novSez.append(k)
matrika = novSez
maxProdukt = 1
for i in range(16):
    for j in range(16):
        prod1 = matrika[i][j]*matrika[i+1][j]*matrika[i+2][j]*matrika[i+3][j]
        if prod1 > maxProdukt:
            maxProdukt = prod1
        prod2 = matrika[i][j]*matrika[i][j+1]*matrika[i][j+2]*matrika[i][j+3]
        if prod2 > maxProdukt:
            maxProdukt = prod2
        prod3 = matrika[i][j]*matrika[i+1][j+1]*matrika[i+2][j+2]*matrika[i+3][j+3]
        if prod3 > maxProdukt:
            maxProdukt = prod3
        prod4 = matrika[19-i][j]*matrika[18-i][j+1]*matrika[17-i][j+2]*matrika[16-i][j+3]
        if prod4 > maxProdukt:
            maxProdukt = prod4
#print(maxProdukt)

#problem12
import math
def divisors(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            number_of_factors +=2
        else:
            continue
    return number_of_factors

x=1
for y in range(2,1000000):
    x += y
    if divisors(x) >= 500:
        #print(x)
        break

#problem13
import sys
sys.setrecursionlimit(100000)
dat = 'project_euler_13.txt'
seznam = []
with open(dat) as f:
    for vrstica in f:
        
        seznam.append(vrstica)
seznam = seznam[1:]
vsota = 0
for element in seznam:
    vsota += int(element)
vs = str(vsota)
#print(vs[len(vs) - 10:])

#problem14
def naslednji_clen(n):
    if n % 2 == 1:
        return n * 3 + 1
    else:
        return n // 2

dolzine = {}
dolzine[1] = 1

def dolzina_zaporedja(n):
    if n not in dolzine:
        dolzine[n] = dolzina_zaporedja(naslednji_clen(n)) + 1
    return dolzine[n]

dolzina = 0

for i in range(1,1000000):
    l = dolzina_zaporedja(i)
    if l > dolzina:
        dolzina = l
        clen = i



#problem 15
'''če bi lahko v polj vrstnem redu, bi vsakič mel 2n potez, torej vseh (2n)!,
ampak ker vrstni red ni poljuben, in ker je n vrstic in n stolpcev, je treba s tem delit. torej C(2n,n).
2n premikov, lahko jih zbereš n naenkrat'''
st = math.factorial(40) / (math.factorial(20) * math.factorial(20)) 
#print(st)


#problem 16
potenca = 2 ** 1000
vsota = 0
while potenca > 0:
    vsota += potenca % 10
    potenca //= 10
#problem 17
do_19 = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
desetice = [0,3,6,6,5,5,5,7,6,6]
hundred = 7
one_thousand = 11
vsota = 0
_and_ = 3
for i in range(1,1001):
    e = i % 10
    d = i // 10 % 10
    s = i // 100 % 10
    t = i // 1000 % 10
    if t != 0:
        vsota += one_thousand
    if i % 1000 != 0:
        if s != 0:
            vsota += do_19[s] + hundred
            if i % 100 != 0:
                vsota += _and_
        if i % 100 != 0:
            if d < 2:
                vsota += do_19[i%100]
            else:
                vsota += desetice[d]
                if e != 0:
                    vsota += do_19[e]
# problem 18
datoteka_1 = 'project_euler_18.txt'
seznam = []
with open(datoteka_1) as f:
    for vrstica in f:
        seznam.append(vrstica)
stevila = []
for i in seznam:
    j = i.split(' ')
    k = [int(x) for x in j]
    stevila.append(k)
stevila = stevila[::-1]

def najvecja_pot(trikotnik):
    trenutna_vsota = []
    if len(trikotnik) == 1:
        return trikotnik
    else:
        for i in range(len(trikotnik[1])):
            vsota1 = trikotnik[1][i] + trikotnik[0][i]
            vsota2 = trikotnik[1][i] + trikotnik[0][i+1]
            if vsota2 > vsota1:
                trenutna_vsota.append(vsota2)
            else:
                trenutna_vsota.append(vsota1)
        trikotnik.pop(0)
        trikotnik.pop(0)
        trikotnik.insert(0, trenutna_vsota)
        return najvecja_pot(trikotnik)
#print(najvecja_pot(stevila))

#problem 19
from datetime import *

stevec = 0
leto = 1901
mesec = 1

trenutni = date(leto,mesec,1)

while trenutni.year < 2001:
	if trenutni.weekday() == 6:
		stevec += 1
	if trenutni.month == 12:
		mesec = 1
		leto += 1
	else:
		mesec += 1
	trenutni = date(leto,mesec,1)

#problem 20
stevilo = math.factorial(100)
vsota = 0
while stevilo > 0:
    vsota += stevilo % 10
    stevilo //= 10


