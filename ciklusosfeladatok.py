import math
import random

def feladat1():
    # 1. írjuk ki a számokat 100-tól 1-ig visszafelé, 1 sorba 10 szám kerüljön
    szamlalo = 0
    for i in range(100,0,-1):
        print(i, end=" ")
        szamlalo += 1
        if szamlalo == 10:
            print("\n")
            szamlalo = 0

def feladat2():
    for i in range(0,151,2):
        if i%2 == 0:
            print(i, end=" ")

def feladat3():
    for i in range(0,151,1):
        print(i**2)

def feladat4():
    szam = float(input("Adj meg egy számot! "))
    oszto = szam
    while oszto > 0:
        if szam%oszto == 0:
            print(int(oszto))
        oszto -= 1

def feladat5():
    for i in range(1,15):
        szam = randint(1,3)
        if szam == 3:
            szam = "X"
        if i == 14:
            i = "13+1"
        print(str(i)+". tipp: "+str(szam))

def feladat6():
    szam = int(input("Adj meg egy egész számot! "))
    faktorialis = 1
    for i in range(1,szam+1):
        faktorialis = faktorialis * i
    print(faktorialis)

def feladat7():
    szam = 0
    for i in range(101):
        szam = szam + i
    print (szam)

def feladat8():
    f1 = 0
    f2 = 1

    fibonacci = 0
    for i in range(81):
        if i < 2:
            n = i
        else:
            n = n-1 + n-2
        print(n)

def feladat9():
    print("  ", end="")
    for i in range(1,11):
        print(i, end=" ")

    print("\n", end="")

    for i in range(1,11):
        print(i, end=" ")
        for j in range(1,11):
            print(j*i, end=" ")
        print("\n", end="")

def feladat10():
    for i in range(1,11):
        veletlenszam = random.randint(20, 30)
        print(str(i) + ". szám: " + str(veletlenszam))

def feladat11():
    for i in range(1,6):
        lottoszam = random.randint(1, 90)
        print(str(i) + ". szám: " + str(lottoszam))

def feladat12():
    for i in range(101,1000):
        if i%3 == 0:
            print(i)

def feladat13():
    for i in range(-99,-9,1):
        print(i)

def feladat14():
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
    maxszam = 100
    for i in range(1,maxszam+1):
        osztok = 0
        for j in range(1,maxszam+1):
            if i%j == 0:
                osztok += 1
        if osztok == 2:
            print(i)

def feladat16():
    negyzetszam = 0
    for i in range(1,11):
        negyzetszam += i**2
    print(negyzetszam)

def feladat17():
    osszeg = 0
    for i in range(10):
        szam = random.randint(1,10)
        osszeg = osszeg + szam
        print(szam)
    print("A számok összege: "+str(osszeg))

def feladat18():
    paros = 0
    for i in range(10):
        szam = random.randint(1,10)
        if szam%2 == 0:
            paros += 1
        print(szam)
    print("Ennyi páros szám van köztük: "+str(paros))
