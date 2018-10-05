a = 999
b = 999
while b > 1:
    while a > 1:
        d = list(map(int, str(a * b))) #'int' = créer une liste nommée 'd', 'map' = version simpli d'1 boucle for pour prendre tous les chiffres du nombre, et les transf en 'int'
        if d == d[::-1]:
            print(d)
            print(a)
            print(b)
            break
        a -=1
    a = 999
    b -= 1