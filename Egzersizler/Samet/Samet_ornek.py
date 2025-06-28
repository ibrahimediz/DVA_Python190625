
# pythonda kullanılan değişkenlerden birer örnek tanımlama yapınız


# iki açısı kullanıcı tarafından girilen bir üçgeninn tipini ekrana yazdıran python kodunu yazınız
# 45 - 45 ==> ikizkenar dik üçgen


liste = ["Can","Mursit","AhmetErdem","Elif","Fatma","MehmetAli","Merve","Niyazi","Salih","Samet","Sefa","Tugce","Aysenur","Cevaplar"]
from random import randint

# yukarıda yer alan kod satırlarından faydalanarak rastgele 3 kişinin ismini veren bir generator fonksiyon yazınız
# def sansli(*args):
#    for i in range(3):
#        yield args[randint(0,len(args)-1)]

# for item in sansli(*liste):
#    print(item)

class Cokgen:
    def __init__(self, adi, kenarsayisi, *args, **kwargs):
        self.adi = adi
        self.kenarsayisi = kenarsayisi
        
    def bilgiVer(self):
        print("#"*30)
        print(self.adi)
        print(self.kenarsayisi)
        print(f"İç Açı Toplamı {(self.kenarsayisi-2)*180}")
        print("#"*30)

ucgen = Cokgen("Üçgen", 3)
kare = Cokgen("Kare", 4)
ucgen.bilgiVer()
kare.bilgiVer()
        