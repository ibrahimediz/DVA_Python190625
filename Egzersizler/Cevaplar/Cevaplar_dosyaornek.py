
l1 = ["ankara","istanbul","izmir","antalya","bursa"]
l2 = ["ali","ayşe","fatma","veli","şermin"]
l3 = [200,400,611,855,1100]
from random import choice
import pathlib
yol = pathlib.Path().absolute() / "Egzersizler" / "Cevaplar" / "dosyaornek.csv"
# yol = pathlib.Path().absolute().parent / "dosyaornek.csv"
# # yukarıda yer alan kod satırlarından faydalanarak dosyaornek.csv dosyasına en az 30 satırlık bir veri kaydediniz
dosya = open(yol,"a+",encoding="utf-8")
for i in range(30):
    print(f"{choice(l1)},{choice(l2)},{choice(l3)}",file=dosya)