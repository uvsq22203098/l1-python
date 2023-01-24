def occurence(liste: list):
    """renvoie le nombre d'occurence de chaque lettres dans une expression"""
    occu = 0
    for i in range (len(liste)):
        n = i + 1
        if i == n:
            occu += 1
            print("il y a", occu, "fois", i, "dans", liste)

occurence("coucou")