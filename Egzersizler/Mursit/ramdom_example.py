from random import randint

liste = ["Can", "Mursit", "AhmetErdem", "Elif", "Fatma", "MehmetAli",
         "Merve", "Niyazi", "Salih", "Samet", "Sefa", "Tugce", "Aysenur", "Cevaplar"]

def rastgele_kisiler():
    secilen = []
    while len(secilen) < 3:
        i = randint(0, len(liste) - 1)
        if i not in secilen:
            secilen.append(i)
            yield liste[i]

for isim in rastgele_kisiler():
    print(isim)

