liste = ["Can","Mursit","AhmetErdem","Elif","Fatma","MehmetAli","Merve","Niyazi","Salih","Samet","Sefa","Tugce","Aysenur","Cevaplar"]
import os
fileName = "ornek.py"
soru = """
# iki açısı kullanıcı tarafından girilen bir üçgeninn tipini ekrana yazdıran python kodunu yazınız
# 45 - 45 ==> ikizkenar dik üçgen
"""
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
        os.mkdir(f"Egzersizler/{item}")
    dosya = open(f"Egzersizler/{item}/{item}_{fileName}","a+")
    print(soru,file=dosya)
    