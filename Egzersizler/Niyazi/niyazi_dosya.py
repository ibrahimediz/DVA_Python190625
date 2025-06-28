class Araba:
    marka = "Mercedes" 

    def __init__(self, model, alici):
        self.model = model  
        self.alici = alici
        print(f"{Araba.marka} markalı bir araç oluşturuldu.")

    def satinAl(self):
        print(f"{self.alici}, {self.model} model aracı satın aldı.")

    @classmethod
    def markaBilgisi(cls):
        print(f"Bu araçların markası: {cls.marka}")



arac1 = Araba("C200", "Ali")
arac2 = Araba("E300", "Ayşe")

arac1.satinAl()
arac2.satinAl()

arac1.markaBilgisi()
arac2.markaBilgisi()
