#N = [] -> suite des chiffres de N -> besoin de: cf ci dessous:
        #n = int -> list chiffre n ???
# donc test avec une suite basic et une multiplication de 2 chiffres a la suite au lieu de 5
n = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,3,4,3,2,5,6,5,6,5,4,4,4,4,4,4,2]
a = 0
i = 0
test = 0
while i < int(len(n)-1):
    test = int(int(int(n[i]) * int(n[i + 1])) * int(int(n[i + 2]) * int(n[i + +3])) * int((n[i + 4])))
    if test > a:
        a = int((int(n[i])*int(n[i+1]))*int(int(n[i+2])*int(n[i++3]))*int(n[i+4]))
    i += 1

print("\n", a)


