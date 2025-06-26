import json.tool
import sqlite3 as sql
import csv,json
import pathlib as pt 

yol = pt.Path().absolute() / "Dokumanlar" / "DosyaIslemleri" / "DB" / "chinook.db"
# print(yol)
con = sql.connect(yol)
cursor = con.cursor()
sorgu = """
SELECT 
art.Name as ArtistName,
alb.Title as AlbumName,
tr.Name as TrackName
FROM artists as art
LEFT JOIN albums as alb ON art.ArtistId = alb.ArtistId
LEFT JOIN tracks as tr ON alb.AlbumId = tr.AlbumId
"""

cursor.execute(sorgu)
sonuc = cursor.fetchall()
# print(sonuc)
# with open(pt.Path().absolute() / "Dokumanlar" / "DosyaIslemleri" / "DB" / "chinook.csv","w",encoding="utf-8") as dosya:
#     for item in sonuc:
#         print(f"{item[0]},{item[1]},{item[2]}",file=dosya)
# # ('Mela Tenenbaum, Pro Musica Prague & Richard Kapp', 'Locatelli: Concertos for Violin, Strings and Continuo, Vol. 3', 'Concerto for Violin, Strings and Continuo in G Major, Op. 3, No. 9: I. Allegro')



# with open(pt.Path().absolute() / "Dokumanlar" / "DosyaIslemleri" / "DB" / "chinook2.csv","w",encoding="utf-8") as dosya:
#     oku = csv.writer(dosya)
#     header = ["ArtistName","AlbumName","TrackName"]
#     oku.writerow(header)
#     oku.writerows(sonuc)


with open(pt.Path().absolute() / "Dokumanlar" / "DosyaIslemleri" / "DB" / "chinook2.csv","r",encoding="utf-8") as dosya, \
     open(pt.Path().absolute() / "Dokumanlar" / "DosyaIslemleri" / "DB" / "chinook3.json","w",encoding="utf-8") as dosya2:
    oku = csv.reader(dosya)
    okunan = list(oku)
    header = okunan[0]
    sonuc = []
    for item in okunan[1:]:
        sozluk = dict.fromkeys(header,[item])
        sonuc.append(sozluk)
    json.dump(sonuc,dosya2)

