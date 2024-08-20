# Exercise 2:
# 1
def facto(p):
    if p == 0:
        return 1
    return p * facto(p - 1)

# 2
def product(n, k):
    if n == 0 or k == 0:
        return 1
    elif n >= k:
        resultat = 1  
        for i in range(1, k + 1):
            resultat *= n - (i - 1)
        return resultat

# 3
def binomial(n, k):
    if n == 0 or k == 0:
        return 1
    elif n >= k:
        return produit(n, k) // facto(k)

# 4
def array_binomiaux(n):
    liste = []
    for i in range(1, n + 1):
        liste.append(binomial(n, i))
    return liste

# Exercise 1:
def drawing(ch):
    for i in range(1, len(ch) + 1):
        for j in range(i - 1, len(ch)):
            print(ch[j], end="")
        print()
    for i in range(1, len(ch) + 1):
        for j in range(i):
            print(ch[j], end="")
        print()

drawing("Programming")

# Exercise 3:
def BubbleSort(liste):
    for i in range(len(liste)):
        for j in range(len(liste) - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

liste = [34, 12, 22, 11, 64, 90]
sorted_liste = BubbleSort(liste)
print(sorted_liste)



