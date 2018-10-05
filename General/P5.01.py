tst = 0
a = 2520
while True:
    for i in range(11, 21):
        if a % i == 0:
            tst += 1
        else:
            break
    if tst == 10:
        break
    tst = 0
    a += 1
print(a)
import time
print(time.perf_counter())