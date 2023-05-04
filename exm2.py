from num2words import num2words
import inflect

p = inflect.engine()

sayi = input("Sayi giriniz: ")
yazi = num2words(sayi, lang='tr')

rakamlar = []
for kelime in yazi.split():
    if kelime.isdigit():
        rakamlar.append(p.number_to_words(kelime, zero='sıfır'))
    else:
        rakamlar.append(kelime)

print(' '.join(rakamlar))