import math
import time

z = 600851475143
b = 0
i = 1
while i < math.sqrt(z):                                         # essayer de i=0 à i=sqrt(z)
    if z % i == 0 and (3 ** i - 3) % i == 0:                    # si i divise z et (3^i - 3) divisible par i (petit théorème de fermat)
        e = i                                                   # prendre i et le stocker dans e
    if int((i / (math.sqrt(z))) * 100) != b:                    # si le pourcentage n'est pas le même que celui d'avant
        b = int((i / (math.sqrt(z))) * 100)                     # stocker en b le pourcentage d'avancement de i (règle de trois)
        print('\r[', b + 1, '% ]', end='')                      # afficher pourcentage n'est pas le même que celui d'avant
        time.sleep(0.01)
    i += 1
print('\r', e)
