a = 1
sc = 0
cs = 0

while a <= 100 :
    cs += a
    sc += a**2
    a += 1
cs = cs ** 2
print ('somme des carrés', sc)
print ('carré de la somme', cs)

dif = cs-sc

print ('\nDifférence "la somme des carrés" - "le carré de leur somme" est', dif )



while i < int(len(n)-1):
    if int(n[i])*int(n[i+1]) > a:
        a = int(n[i])*int(n[i+1])
    i += 1
print ("\n", a)