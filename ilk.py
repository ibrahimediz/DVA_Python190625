liste = ["Can","Mursit","AhmetErdem","Elif","Fatma","MehmetAli","Merve","Niyazi","Salih","Samet","Sefa","Tugce","Aysenur","Cevaplar"]
import os
fileName = "ornek.py"
soru = """
# pythonda kullanılan değişkenlerden birer örnek tanımlama yapınız
"""
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
        os.mkdir(f"Egzersizler/{item}")
    dosya = open(f"Egzersizler/{item}/{item}_{fileName}","a+")
    print(soru,file=dosya)
    