#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

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
    