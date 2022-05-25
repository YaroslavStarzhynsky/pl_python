#file = open("przyklad.txt").readlines()
file = open("liczby.txt").readlines()
line = []
for lines in file:
    line.append(int(lines[:-1]))
line = list(set(line))
trojki = []
for liczba in line:
    for frst in line:
        if liczba != frst and liczba % frst == 0:
            for scnd in line:
                if scnd != frst and frst % scnd == 0:
                    trojki.append(str([scnd, frst, liczba]))

pietki = []
for liczba in line:
    for frst in line:
        if liczba != frst and liczba % frst == 0:
            for scnd in line:
                if scnd != frst and frst % scnd == 0:
                    for thrd in line:
                        if thrd != scnd and scnd % thrd == 0:
                            for frth in line:
                                if frth != thrd and thrd % frth == 0:
                                    pietki.append(str([frth, thrd, scnd, frst, liczba]))

print("a)" , str(len(trojki)), sep =' ')
print("b)" , str(len(pietki)), sep =' ')