def poprawna(pesel):
    suma = 0
    suma = (int(pesel[0])*1 + int(pesel[1])*3 + int(pesel[2])*7 + int(pesel[3])*9 + int(pesel[4])*1 + int(pesel[5])*3 + int(pesel[6])*7+int(pesel[7])*9+int(pesel[8])*1+ int(pesel[9])*3+int(pesel[10]))
    return suma

file = open("przyklad.txt", "r")
pesel = []
with open("dane.txt", "r") as f:
    for line in f.readlines():
        pesel.append(line)

#zadanie 6_1
kobiet = 0
mezczyzn = 0
with open("dane.txt", "r") as f:
    for line in f.readlines():
        if(int(line[9])%2==0):
            kobiet+=1
        else:
            mezczyzn+=1
print(kobiet, mezczyzn)
# 442 558

#zadanie 6_2
counter = 0
for i in pesel:
    m = int(i[2:4])
    if m > 12:
        m=m-20
    if(m==11):
        counter+=1

print(counter)
#90

#zadanie 6_3
blend = []
with open("dane.txt", "r") as f:
    for line in f.readlines():
        if(poprawna(line)%10!=0):
            blend.append(line)
print(blend)
