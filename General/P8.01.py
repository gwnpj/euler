#N = [] -> suite des chiffres de N -> besoin de: cf ci dessous:
        #n = int -> list chiffre n ???
# donc test avec une suite basic et une multiplication de 2 chiffres a la suite au lieu de 5
n = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
a = 0
i = 0
while i < int(len(n)-1):
    if int(n[i])*int(n[i+1]) > a:
        a = int(n[i])*int(n[i+1])
    i += 1
print (a)