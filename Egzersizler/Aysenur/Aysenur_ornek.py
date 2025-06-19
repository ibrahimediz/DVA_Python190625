
# pythonda kullanılan değişkenlerden birer örnek tanımlama yapınız


# iki açısı kullanıcı tarafından girilen bir üçgeninn tipini ekrana yazdıran python kodunu yazınız
# 45 - 45 ==> ikizkenar dik üçgen
a = int(input("1. açı: "))
b = int(input("2. açı: "))


# Geçerli üçgen mi kontrolü
if  a <= 0 or b <= 0:
    print("Geçersiz açı pozitif olmalı.")
else:
    # Üçgen tipi belirleme
    if a == b and a == 45:
        print("İkizkenar dik üçgen")
    elif a == b or a == 60:
        print("Eşkenar üçgen")
    else:
        print("Belirsiz")