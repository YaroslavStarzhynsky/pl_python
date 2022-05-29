file = open("liczby.txt").read().split()
# print(liczby_str)
numbers = [int(element) for element in file]
sortnum = sorted(numbers)
# print(sort_liczby)
three = []
five = []
for frst in sortnum:
    for scnd in sortnum:
        if scnd > frst:
            if scnd % frst == 0:
                for thrd in sortnum:
                    if thrd > scnd:
                        if thrd % scnd == 0:
                            tempthree = []
                            tempthree.append(frst)
                            tempthree.append(scnd)
                            tempthree.append(thrd)
                            three.append(tempthree)
                            for frth in sortnum:
                                if frth > thrd:
                                    if frth % thrd == 0:
                                        for ffth in sortnum:
                                            if ffth > frth:
                                                if ffth % frth == 0:
                                                    tempfive = []
                                                    tempfive.append(frst)
                                                    tempfive.append(scnd)
                                                    tempfive.append(thrd)
                                                    tempfive.append(frth)
                                                    tempfive.append(ffth)
                                                    five.append(tempfive)
print("a)", len(three),sep=' ')
print("b)", len(five),sep=' ')

