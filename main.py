plik = open("przyklad.txt",'r')
dane = plik.read().split("\n\n")
dzialki = []
for line in dane:
    lineso = line.split("\n")
    dzialki.append(lineso)
print(dzialki)
counter = 0
countertraw = 0
for i in range(len(dane)):
    for j in range(0, len(dane[i])):
        if(dane[i][j] == '*'):
            counter+=1
    if(counter/900>=0.7):
        countertraw+=1
        counter = 0

print(countertraw)


# 4.2

square = [0,0]
for i in range(len(dzialki)):
    temp = dzialki[i]
    rotate = ""
    for i in range()
