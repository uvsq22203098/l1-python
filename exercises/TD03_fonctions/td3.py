
def tempsEnSeconde(temps):
    # Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde.
    s = 24*3600 * temps[0] + 3600 * temps[1] + 60 * temps[2] + temps[3]
    return s

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   



def secondeEnTemps(seconde):
    # Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument
    j = seconde // (24 * 3600)
    r = seconde % (24 * 3600)
    h = r // 3600
    r = r % 3600
    m = r // 60
    s = r % 60

    return ((j, h, m, s))

temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")



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

print()
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
    print()
    afficheTemps(secondeEnTemps(tempsT))


sommeTemps((2,3,4,25),(5,22,57,1))



def proportionTemps(temps, proportion):
    temps = tempsEnSeconde(temps)
    temps = temps * proportion
    temps = secondeEnTemps(temps)
    return temps

print()
afficheTemps(proportionTemps((2,0,36,0),0.2))



def tempsEnDate(temps):
    an0 = 1970
    mois0 = 1
    jour0 = 1

    if temps[0] >= 365:
        an0 = an0 + temps[0] // 365
        jour0 = jour0 % 365
    else:
        jour0 = temps[0] + jour0

    if jour0 > 30:
        mois0 = mois0 + jour0 // 30
        jour0 = jour0 % 30
    
    return (an0, mois0, jour0, temps[1], temps[2], temps[3])

def afficheDate(date):
    print(date[2],end=" ")
    
    if date[1] == 1:
        print("janvier", end=" ")
    if date[1] == 2:
        print("février", end=" ")
    if date[1] == 3:
        print("mars", end=" ")
    if date[1] == 4:
        print("avril", end=" ")
    if date[1] == 5:
        print("mai", end=" ")
    if date[1] == 6:
        print("juin", end=" ")
    if date[1] == 7:
        print("juillet", end=" ")
    if date[1] == 8:
        print("aout", end=" ")
    if date[1] == 9:
        print("septembre", end=" ")
    if date[1] == 10:
        print("octobre", end=" ")
    if date[1] == 11:
        print("novembre", end=" ")
    if date[1] == 12:
        print("décembre", end=" ")

    print(date[0], end="")

    print("a", date[3], ":", date[4], ":", date[5])

temps = secondeEnTemps(1000000000)
print()
afficheTemps(temps)
print()
afficheDate(tempsEnDate(temps))


#tester ici les fonctions de la librairie time



