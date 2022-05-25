# file = open("przyklad.txt").readlines()
file = open("liczby.txt").readlines()
mass = []
liczba = []
massdiff = []
for line in file:
    temp = int(line[:-1])
    roz = []
    czynnik = 2
    liczba.append(temp)
    while temp != 1:
        if temp % czynnik == 0:
            temp = int(temp / czynnik)
            roz.append(czynnik)
            czynnik = 2
        else:
            czynnik += 1
    mass.append(set(roz))
    massdiff.append(roz)
lenght = []
lenghth = []
for i in massdiff:
    lenght.append(len(i))
for i in mass:
    lenghth.append(len(i))
for i in massdiff:
    if len(i) == max(lenght):
        print(str(liczba[massdiff.index(i)]), str(len(i)), sep=' ')
for i in mass:
    if len(i) == max(lenghth):
        print(str(liczba[mass.index(i)]), str(len(i)), sep=' ')
# 99792 10
# 20992 10
# 56064 10
# 62790 6