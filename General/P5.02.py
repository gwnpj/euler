div = list(range(11, 21))
lcm = div[0]
b = div[1]
pd = lcm * b
j = 0
for i in range(11, 20):
    b = div[(j+1)]
    pd = lcm * b
    while b:
        lcm, b = b, lcm % b
    lcm = int(pd / lcm)
    j += 1
print(lcm)