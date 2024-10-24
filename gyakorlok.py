def woodall():
    max = 11
    for n in range(1,max):
        woodall = n * pow(2, n) - 1
        if n == max-1:
            print(str(woodall))
        else:
            print(str(woodall), end=", ")

def mertanisor():
    # Írd ki a 3 kvóciensú 2 kezdőelemű mértani sor első 6 elemét ponttal elválasztva az utolsó után ne legyen pont.
    # kezdő elem
    a = 2
    # kvóciens
    q  = 3
    # kiírandó elemek száma
    max = 6

    for i in range(max):
        if i == max-1:
            print(str(a))
        else:
            print(str(a), end=", ")
        a = a * q