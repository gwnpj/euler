import math

z = 600851475143
i = 1
while i < math.sqrt(z):                             # essayer de i=0 à i=sqrt(z)
    if z % i == 0 and (3 ** i - 3) % i == 0:        # si i divise z et (3^i - 3) divisible par i (petit théorème de fermat)
        e = i                                       # prendre i et le stocker dans e
    i += 1
print(e)
