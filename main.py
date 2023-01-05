def dilniki(a):
    resulti = 0
    k = 3
    if a % 2==0:
        return False
    while(a > 1):
        if a % k == 0:
            resulti +=1
        while(a % k==0):
            a = a//k
        k = k+2
    if resulti > 3 or resulti<3:
        return False
    if resulti == 3:
        return True

plik = "liczby.txt"
counter = 0
a = []
with open(plik) as file:
    for line in file:
        a.append(int(line[:-1]))
print(a)
for i in range(len(a)):
    if (dilniki(a[i]) == True):
        counter+=1
print(counter)

#wynik 59.1 - 113
#zadanie 59.2

for i in range(len(a))