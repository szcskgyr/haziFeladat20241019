import math
import random

def feladat1():
    # 1. írjuk ki a számokat 100-tól 1-ig visszafelé, 1 sorba 10 szám kerüljön
    szamlalo = 0
    for i in range(100,0,-1):
        print(str(i), end=" ")
        szamlalo += 1
        if szamlalo == 10:
            print("\n")
            szamlalo = 0

def feladat2():
    # 2. Írjuk ki 0-tól 150-ig a páros számokat
    for i in range(0,151,2):
        if i%2 == 0:
            print(str(i), end=" ")

def feladat3():
    # 3. Írjuk ki 0-tól 150-ig a négyzetszámokat
    for i in range(0,151,1):
        print(str(i**2))

def feladat4():
    # 4. Írjuk ki egy bekért szám osztóit
    szam = int(input("Adj meg egy egész számot! "))
    oszto = abs(szam)
    while oszto > 0:
        if szam%oszto == 0:
            print(str(oszto))
        oszto -= 1

def feladat5():
    # 5. Írjuk ki egy TOTÓ szelvény lehetséges kitöltését
    for i in range(1,15):
        szam = randint(1,3)
        # a harmadik lehetőség 3 helyett X legyen
        if szam == 3:
            szam = "X"
        # 14. tipp szöveg cseréje 13+1-re
        if i == 14:
            i = "13+1"
        print(str(i)+". tipp: "+str(szam))

def feladat6():
    # 6. Írjuk ki egy bekért szám faktoriálisát
    szam = int(input("Adj meg egy egész számot! "))
    faktorialis = 1
    for i in range(1,szam+1):
        faktorialis = faktorialis * i
    print(faktorialis)

def feladat7():
    # 7.	Írjuk ki az első 100 szám összegét
    szam = 0
    for i in range(101):
        szam = szam + i
    print (szam)

def feladat8():
    # 8. Írjuk ki a Fibonacci sorozat első 80 elemét
    pass

def feladat9():
    # 9. Írjuk ki a 10x10-es szorzótáblát
    # felső sor kiírása
    print("  ", end="")
    for i in range(1,11):
        print(i, end=" ")
    print("\n", end="")

    # bal oszlop kiírása
    for i in range(1,11):
        print(i, end=" ")
        # szorzatok kiszámítása soronként
        for j in range(1,11):
            print(j*i, end=" ")
        print("\n", end="")

def feladat10():
    # 10.	Írjunk ki 10 véletlen számot! A véletlen számokat a 20-30-as értéktartományban generáljuk!
    for i in range(1,11):
        veletlenszam = random.randint(20, 30)
        print(str(i) + ". szám: " + str(veletlenszam))

def feladat11():
    # 11.	Generáljunk 5 lottószámot! (nem baj, ha van köztük egyforma)
    for i in range(1,6):
        lottoszam = random.randint(1, 90)
        print(str(i) + ". szám: " + str(lottoszam))

def feladat12():
    # 12.	Írjuk ki a hárommal osztható számokat 100 és 1000 között!
    for i in range(101,1000):
        if i%3 == 0:
            print(i)

def feladat13():
    # 13.	Írjuk ki a negatív kétjegyű számokat!
    for i in range(-99,-9,1):
        print(i)

def feladat14():
    # 14.	Írjuk ki a számokat 1-től 100-ig oly módon,hogy ha egy szám 3-mal osztható, akkor a szám helyett írjuk azt, hogy BIM, ha kettővel osztható, akkor írjuk azt, hogy BAMM, és ha 2-vel is és 3-mal is osztható, akkor írjuk, hogy BIM-BAM, egyéb esetben írjuk ki a számot!
    for i in range(1,101):
        if (i%2 == 0) and (i%3 == 0):
            print("BIM-BAM")
        elif i%2 == 0:
            print("BAMM")
        elif i%3 == 0:
            print("BIM")
        else:
            print(i)

def feladat15():
    # 15. Írjuk ki a prím számokat 100-ig!
    maxszam = 100
    for i in range(1,maxszam+1):
        osztok = 0
        # aktuális szám osztóinak megszámolása
        for j in range(1,maxszam+1):
            if i%j == 0:
                osztok += 1
        # két db osztó esetén a szám kiírása
        if osztok == 2:
            print(i)

def feladat16():
    # 16. Írjuk ki az első 10 négyzetszám összegét!
    negyzetszam = 0
    for i in range(1,11):
        negyzetszam += i**2
    print(str(negyzetszam))

def feladat17():
    # 17.	Írjunk ki 1-10 értékhatár közé eső 10 véletlen számot, majd írjuk ki ezek összegét!
    osszeg = 0
    for i in range(1,11):
        szam = random.randint(1,10)
        osszeg = osszeg + szam
        print(str(i) + ". szám: " + str(szam))
    print("A számok összege: "+str(osszeg))

def feladat18():
    # 18.	Írjunk ki 1-10 értékhatár közé eső 10 véletlen számot, s mondjuk meg, hány páros van közöttük!
    paros = 0
    for i in range(1,11):
        szam = random.randint(1,10)
        if szam%2 == 0:
            paros += 1
        print(str(i) + ". szám: " + str(szam))
    print("Ennyi páros szám van köztük: "+str(paros))
