liste = ["Can","Mursit","AhmetErdem","Elif","Fatma","MehmetAli","Merve","Niyazi","Salih","Samet","Sefa","Tugce","Aysenur","Cevaplar"]
import os
fileName = "dosyaornek.py"
soru = """
l1 = ["ankara","istanbul","izmir","antalya","bursa"]
l2 = ["ali","ayşe","fatma","veli","şermin"]
l3 = [200,400,611,855,1100]
from random import choice

# yukarıda yer alan kod satırlarından faydalanarak dosyaornek.csv dosyasına en az 30 satırlık bir veri kaydediniz
"""
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
        os.mkdir(f"Egzersizler/{item}")
    dosya = open(f"Egzersizler/{item}/{item}_{fileName}","a+")
    print(soru,file=dosya)
    