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

for i in range(1,6):
    l = dolzina_zaporedja(i)
    if l > dolzina:
        dolzina = l
        clen = i