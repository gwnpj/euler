i = 0
somme = 0
while True :
    try :
        a = int (input('entrez un nombre\n') )
    except ValueError :
        print('erreur de saisie')
        continue
    else :
        while i < a:
            if i%3 == 0 or i%5 == 0:
                somme += i
            i += 1
        print(somme)
        break