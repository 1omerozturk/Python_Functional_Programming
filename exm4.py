import math
x=int(input("sayi:"))
kare=(lambda x: x*x)(x)
kup=(lambda x: x*x*x)(x)
print(f"karesi= {kare}")
print(f"küpü= {kup}")

radius=float(input("yaricap:"))
alan=(radius**2)*math.pi
print("Alan",alan)


dizi=list(input("Dizi:"))

yenidizi=[i for i in dizi if(i.isupper())]
print(f"Büyük harf sayısı {len(yenidizi)} Küçük harf sayısı:{len(dizi)-len(yenidizi)}")