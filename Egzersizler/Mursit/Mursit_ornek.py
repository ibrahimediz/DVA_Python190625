
# pythonda kullanılan değişkenlerden birer örnek tanımlama yapınız


# iki açısı kullanıcı tarafından girilen bir üçgeninn tipini ekrana yazdıran python kodunu yazınız
# 45 - 45 ==> ikizkenar dik üçgen

def ucgen_tipi_bul():
    try:
        a = float(input("1. açıyı girin: "))
        b = float(input("2. açıyı girin: "))
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
        return

    c = 180 - (a + b)  # üçüncü açı

 
    if a <= 0 or b <= 0 or c <= 0:
        print("Toplamları 180° olan pozitif açılar girilmeli!")
        return

    tipler = []

    # Eşitlik durumları
    eps = 1e-6  # ondalık toleransı
    if abs(a - b) < eps and abs(b - c) < eps:
        tipler.append("eşkenar")
    elif abs(a - b) < eps or abs(a - c) < eps or abs(b - c) < eps:
        tipler.append("ikizkenar")
    else:
        tipler.append("çeşitkenar")

    if abs(a - 90) < eps or abs(b - 90) < eps or abs(c - 90) < eps:
        tipler.append("dik")
    elif a > 90 or b > 90 or c > 90:
        tipler.append("geniş")
    else:
        tipler.append("dar")

    print(" ".join(tipler), "üçgen")

if __name__ == "__main__":
    ucgen_tipi_bul()

liste = ["Can","Mursit","AhmetErdem","Elif","Fatma","MehmetAli","Merve","Niyazi","Salih","Samet","Sefa","Tugce","Aysenur","Cevaplar"]
from random import randint

# yukarıda yer alan kod satırlarından faydalanarak rastgele 3 kişinin ismini veren bir generator fonksiyon yazınız

