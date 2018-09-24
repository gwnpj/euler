a = 999
b = 999
c: int = 1
while b > 1:
    while a > 1:
        if (a*b)%11==0:
            d = list(map(int, str(a*b)))
            if len(d) > 4 and \
                    int(d[0]) == int(d[len(d)-1]) and \
                    int(d[1]) == int(d[len(d)-2]) and \
                    int(d[2]) == int(d[len(d)-3]):
                if c != a * b and c < a * b:
                    c = a * b
        a -=1
    a = 999
    b -= 1
print(c)