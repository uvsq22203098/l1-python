n = 3
# diviser par 2 si pair, multiplier par 3 et ajouter 1 si impair
n1 = 10
n2 = 5
n3 = 16
n4 = 8
n5 = 4
n6 = 2
n7 = 1
n8 = 4

def syracuse(n):
    #Retourne la liste des valeurs de la suite en partant de n jusqu'à 1
    liste = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        liste.append(n)
    return(liste)

print(syracuse(3))



def testeConjecture(n_max):
    #Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max
    for i in range (1, n_max + 1):
        if syracuse(i)[-1] != 1:
            return False
    return True
print(testeConjecture(5))



def tempsVol(n):
    #Retourne le temps de vol de n
    tv = len(syracuse(n)) - 1
    return tv

print("Le temps de vol de", 1, "est", tempsVol(1))



def tempsVolListe(n_max):
    #Retourne la liste de tous les temps de vol de 1 à n_max
    liste = [tempsVol(i) for i in range (1, n_max)] # = liste en compréhension
    """ for i in range (1, n_max):
        liste.append(tempsVol(i)) """
    return liste

print(tempsVolListe(100))



tvl=tempsVolListe(10000)
m=max(tvl)
print(m, tvl.index(m))