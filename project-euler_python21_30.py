#problem22
datoteka = 'project_euler_22.txt'
seznam_imen = []
with open(datoteka) as f:
    for vrstica in f:
        imena = vrstica.split(',')
        for ime in imena:
            seznam_imen.append(ime)
        
seznam_imen = sorted(seznam_imen)
m = ['_','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
vrednosti = list(enumerate(m))
vsota = 0
for ime in seznam_imen:
    vrednost_imena = 0
    for črka in ime:
        for x in vrednosti:
            if črka == x[1]:
                vrednost_imena += x[0]
    vrednost_imena *= (seznam_imen.index(ime) + 1)
    vsota += vrednost_imena
#print(vsota)


#print(stevec)

#problem 25
a = 1
b = 1
i = 2
c = 0

while len(str(c)) != 1000:
    c = a + b
    a = b
    b = c
    i += 1
#print(i)

#problem 42
file = 'project_euler_42.txt'
m = ['_','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
vrednosti = list(enumerate(m))
triangular = []
besede = []
stevec = 0
for i in range(1000):
    st = i * (i + 1) // 2
    triangular.append(st)
with open(file) as f:
    for vrstica in f:
        x = vrstica.split(',')
        for beseda in x:
            besede.append(beseda)
for beseda in besede:
    vsota_besede = 0
    for crka in beseda:
        for par in vrednosti:
            if crka == par[1]:
                vsota_besede += par[0]
    if vsota_besede in triangular:
        stevec += 1

#problem 40
stevilo = '_'
for x in range(1,1000001):
    stevilo += str(x)
produkt = int(stevilo[1]) * int(stevilo[10]) * int(stevilo[100])* int(stevilo[1000]) * int(stevilo[10000]) * int(stevilo[100000]) * int(stevilo[1000000])
print(produkt)

#problem 48
vsota = 0

for i in range(1,1001):
    vsota += i ** i
st = str(vsota)
