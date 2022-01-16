print("----------------------------")
print("Felszín és térfogat számítás")
print("----------------------------")
from decimal import Decimal

test = input("Milyen testet szeretnél kiszámítani ? ( kocka, gömb, téglatest, gúla) ")

if test == "kocka" or test == "Kocka":
    kocka = input("Térfogat vagy felszín számolás ?")
    if kocka == "Térfogat" or kocka == "térfogat":
        kockaO = float(input("Add meg a kocka oldalát:"))
        kterfogat = kockaO**3
        print(round(kterfogat, 2))   
    elif kocka == "Felszín" or kocka == "felszín":
        kockaO = float(input("Add meg a kocka oldalát: "))
        kockafelszin = 6*(kockaO**2)
        print(round(kockafelszin, 2))
    else:
        print("Csak Térfogat vagy felszínt adhatsz meg opcíóként!")

if test == "gömb" or test == "Gömb":
    gömb = input("Térfogat vagy felszín számolás ?")
    if gömb == "Térfogat" or gömb == "térfogat":
        gömbR = float(input("Add meg a sugár nagyságát: "))
        gterfogat = 4*(gömbR**3)*3.14/3
        print(round(gterfogat, 2))
    elif gömb == "Felszín" or gömb == "felszín":
        gömbR = float(input("Add meg a sugár nagyságát: "))
        gfelszin = 4*(gömbR**2)*3.14
        print(round(gfelszin, 2))
    else:
        print("Csak Térfogat vagy felszínt adhatsz meg opcíóként!")

if test == "téglatest" or test == "Téglatest":
    téglatest = input("Térfogat vagy felszín számolás ?")
    if téglatest == "Térfogat" or téglatest == "térfogat":
        téglatest_a = float(input("Add meg a téglatest /a/ oldalát: "))
        téglatest_b = float(input("Add meg a téglatest /b/ oldalát: "))
        téglatest_c = float(input("Add meg a téglatest /c/ oldalát: "))
        téglatest_terfogat = téglatest_a*téglatest_b*téglatest_c
        print(téglatest_terfogat)
    elif téglatest == "Felszín" or téglatest == "felszín":
        téglatest_a = float(input("Add meg a téglatest /a/ oldalát: "))
        téglatest_b = float(input("Add meg a téglatest /b/ oldalát: "))
        téglatest_c = float(input("Add meg a téglatest /c/ oldalát: "))
        téglatest_felszin = 2*(téglatest_a*téglatest_b+téglatest_a*téglatest_c+téglatest_b*téglatest_c)
        print(round(téglatest_felszin, 2))
    else:
        print("Csak Térfogat vagy felszínt adhatsz meg opcíóként!")

if test == "Gúla" or test == "gúla":
    gúla = input("Térfogat vagy felszín számolás ?")
    if gúla == "Térfogat" or gúla == "térfogat":
        gúla_alapterület = int(input("Add meg a gúla alapjának területét: "))
        gúla_magasság = int(input("Add meg a gúla magasságát: "))
        gúla_térfogat = gúla_alapterület*gúla_magasság/3
        print(round(gúla_térfogat, 2))
    elif gúla == "Felszín" or gúla == "felszín":
        gúla_alapterület = int(input("Add meg a gúla alapjának területét: "))        
        gúla_palást = int(input("Add meg a gúla palástját: "))
        gúla_felszín = gúla_palást+gúla_alapterület
        print(round(gúla_felszín, 2))
    else:
        print("Csak Térfogat vagy felszínt adhatsz meg opcíóként!")    