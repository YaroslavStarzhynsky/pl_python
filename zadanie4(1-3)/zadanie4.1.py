file = open("przyklad.txt").readlines()
#file = open("liczby.txt").readlines()
counter = 0
count = 0
first = False
for line in file:
    temp = line[:-1]
    if temp[0] == temp[-1]:
        if not first:
            count = temp
            first = True
        counter += 1
print(counter, count, sep=', ')  # 93639, 18