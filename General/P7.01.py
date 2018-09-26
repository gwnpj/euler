import time
z = 2
i = 1
while i < 10001:
    while (3**z - 3)%z == 0 and z%2 == 1:
        c = z
        i += 1
        z += 1
    z += 1
print (c)

minu = round((time.perf_counter()/60),2)
seco = (minu - int (minu) ) * 60
print('(en', int(minu),'min et', int(seco), 'sec)')


#NE MARCHE PAS ENCORE COMME JE VOUDRAIS
