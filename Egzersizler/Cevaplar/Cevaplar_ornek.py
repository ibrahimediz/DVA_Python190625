
# iki açısı kullanıcı tarafından girilen bir üçgeninn tipini ekrana yazdıran python kodunu yazınız
# 45 - 45 ==> ikizkenar dik üçgen

aci1 = input("1. Açıyı Giriniz:")
aci2 = input("2. Açıyı Giriniz:")
if aci1 and aci2:
    if aci1.isdigit() and aci2.isdigit():
        aci1,aci2 = int(aci1),int(aci2)
        l1 = [aci1,aci2,180-(aci1+aci2)]
        if sum(l1) == 180:
            k1 = set(l1)
            if len(k1) == 2:
                print("İkizkenar Üçgen")
            elif len(k1) == 1:
                print("Eşkenar Üçgen")
            else:
                print("Çeşit kenar üçgen")
            if 90 in k1:
                print("Dik Üçgen")
        else:
            print("Açılar Hatalı")
    else:
        print("Açılar Sayı olmalıdır")
else:
    print("Giriş Yapılmadı")

