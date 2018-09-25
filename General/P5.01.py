tst = 0
a = 1
while True:
    for i in range(11, 21):
        if a % i == 0:
            tst += 1
    if tst == 10:
        break
    tst = 0
    a += 1
print(a)
