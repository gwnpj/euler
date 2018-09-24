import math
import sys
from time import sleep
z = 600851475143
b = 0
i = 1
while i < math.sqrt(z):
    if z%i == 0:
        if (3**i - 3)%i != 0:
            u = 0
        else:
            e = i
    if i > 6857 and int((i/(math.sqrt(z)))*100) != b:
        b = int((i/(math.sqrt(z)))*100)
        sys.stdout.write('\r')
        sys.stdout.write(str(b+1))
        sys.stdout.write('%')
        sys.stdout.flush()
        sleep(0.01)
    i += 1
print ('\r', e)