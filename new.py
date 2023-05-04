"""
1.Örnek

Bir dikdörtgen sinifi oluşturma ve baslangic fonksiyonu
olarak genislik ve uzunluk pramatrelerini alarak geriye 
dikdortgenin alani dondurur.

"""

class Dikdortgen:
    def __init__(self,x,y):
        return print(x*y)
     
a=Dikdortgen(5,4)
print(a)
 

"""
2. Örnek 

bir dize girilmesi ve geriye ise dizeyi buyuk karakter
olarak geri veren iki fonksiyonlu bir sinif olusturuldu.

"""

class String:
    def getString():
       global dize
       dize=input("Dize girin:")
       return ""
    
    def printString():
        return dize.upper()
        
        
print(String.getString())
print(String.printString())

 
 
 
""" 
#  3. Örnek

Girilen sayinin kac basamakli oldugunu geri veren bir fonksiyon.

 """
s=int(input("Sayi: "))
def sayi(s,basamak=0):
    if s==0:
        return basamak
    else:
        return sayi(s // 10,basamak=basamak+1)

sonuc=sayi(s)
print(sonuc)
