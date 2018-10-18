a = 1
sc = 0
cs = 0
while a <= 100 :
    cs += a
    sc += a**2
    a += 1
cs = cs ** 2
print (cs-sc)