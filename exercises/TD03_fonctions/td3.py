#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

from errno import EEXIST


def tempsEnSeconde(temps):
    """Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    s = 24*3600 * temps[0] + 3600 * temps[1] + 60 * temps[2] + temps[3]
    return s

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   




def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    j = seconde // (24 * 3600)
    r = seconde % (24 * 3600)
    h = r // 3600
    r = r % 3600
    m = r // 60
    s = r % 60

    return ((j, h, m, s))

temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")




"""
def afficheTemps(temps):
    # met le mot au pluriel si sa valeur est supérieure a 1, dans le cas contraire au singulier, sinon elle affichera rien
    if temps[0] > 1:
        print(temps[0],"jours", end=" ")
    elif temps[0] == 1:
        print(temps[0],"jour", end=" ")
    if temps[1] > 1:
        print(temps[1],"heures", end=" ")
    elif temps[1] == 1:
        print(temps[1],"heure", end=" ")
    if temps[2] > 1:
        print(temps[2],"minutes", end=" ")
    elif temps[2] == 1:
        print(temps[2],"minute", end=" ")
    if temps[3] > 1:
        print(temps[3],"secondes", end=" ")
    elif temps[3] == 1:
        print(temps[3],"seconde", end=" ")

afficheTemps((1,0,14,23))
"""




def pluriel(n, mot):
    # permet de donner le pluriel d'un mot lorsqu'il admet une valeur > 1 
    if int(n) > 1:
        print(n, mot + "s", end=" ")
    elif n == 1:
        print(n, mot, end=" ")

def afficheTemps(temps):
    # affiche le nombre de jour, d'heure, de minute, de seconde en respectant l'accord
    pluriel(temps[0], "jour")
    pluriel(temps[1], "heure")
    pluriel(temps[2], "minute")
    pluriel(temps[3], "seconde")

afficheTemps((1,0,14,23))




def demandeTemps():
    jour, heure, minute, seconde = input("\ncombien de jours ?\n"), 70, 70, 70
    while heure >= 24:
        heure = int(input("combien d'heure(s) ?\n"))
        if heure >= 24:
            print("erreur")
    while minute >= 60:
        minute = int(input("combien de minute(s) ?\n"))
        if minute >= 60:
            print("erreur")
    while seconde >= 60:
        seconde = int(input("combien de seconde?\n"))
        if seconde >= 60:
            print("erreur")

    return jour, heure, minute, seconde

afficheTemps(demandeTemps())




def sommeTemps(temps1,temps2):
    tempsT = tempsEnSeconde(temps1) + tempsEnSeconde(temps2)
    afficheTemps(secondeEnTemps(tempsT))

sommeTemps((2,3,4,25),(5,22,57,1))




