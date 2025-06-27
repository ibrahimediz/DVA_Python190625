
# pythonda kullanılan değişkenlerden birer örnek tanımlama yapınız


# iki açısı kullanıcı tarafından girilen bir üçgeninn tipini ekrana yazdıran python kodunu yazınız
# 45 - 45 ==> ikizkenar dik üçgen


liste = ["Can","Mursit","AhmetErdem","Elif","Fatma","MehmetAli","Merve","Niyazi","Salih","Samet","Sefa","Tugce","Aysenur","Cevaplar"]
from random import randint 

# yukarıda yer alan kod satırlarından faydalanarak rastgele 3 kişinin ismini veren bir generator fonksiyon yazınız
def rasgele(*args):
    for i in range(3):
        yield args[randint(0,len(args)-1)]

for i in rasgele(*liste):
    print(i)
        


def rasgele(*args):
    k=[]
    for i in range(3):
        k= args[randint(0,len(args)-1)]
        return k

for i in rasgele(liste):
    print(i)




