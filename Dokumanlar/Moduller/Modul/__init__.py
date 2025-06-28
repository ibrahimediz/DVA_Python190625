class Sinif1:
    def __init__(self):
        """
        Sinif1 classini init fonskiyonu
        """
        print("Sinif1")


def fonk():
    print("fonk 1")
    print(__name__)

if __name__ == "__main__":
    fonk()