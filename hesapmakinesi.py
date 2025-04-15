def hesap_makinesi(sayi1, sayi2):
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    if sayi2 != 0:
        bolum = sayi1 / sayi2
    else:
        bolum = "Tanımsız"
    return toplam, fark, carpim, bolum

def palindrom_kontrol(kelime):
    return kelime == kelime[::-1]

def yas_hesapla(yas):
    return 100 - yas

t, f, c, b = hesap_makinesi(10, 5)
print("Toplam:", t)
print("Fark:", f)
print("Çarpım:", c)
print("Bölüm:", b)

print(palindrom_kontrol("kek"))
print(palindrom_kontrol("masa"))

print("100 yaşına", yas_hesapla(25), "yıl sonra ulaşırsın.") 
