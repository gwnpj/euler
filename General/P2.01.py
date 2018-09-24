lucas = []
i = 0
somme = 2
while True:
    if i < 3:
        lucas.append(i) #ajouter la valeur à la suite de la liste
    else:
        lucas.append((lucas[i-2])+(lucas[i-1]))
        if lucas[i] > 4*(10**6):
            break
        if lucas[i]%2 == 0:
            somme += lucas[i]
    i += 1
print(somme)