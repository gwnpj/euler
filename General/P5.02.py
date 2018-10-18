lcm = 11
for i in range(11, 20):
    b = i + 1
    pd = lcm * b
    while b:
        lcm, b = b, lcm % b
    lcm = int(pd / lcm)
print(lcm)