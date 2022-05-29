#file = open("przyklad.txt").read().split()
file = open("liczby.txt").read().split()
numbers = [int(element) for element in file]
number = []
numberswith = []
numberfrst = []
a = 0
b = 0
numa = 0
numb = 0
for i in range(2, max(numbers) + 1):
    tmp = True
    for y in range(2, int(pow(i, .5) + 1)):
        if i % y == 0:
            tmp = False
            break
    if tmp:
        numberfrst.append(i)

for j in numbers:
    linumbers = []
    for frst in numberfrst:
        if frst > j:
            break
        while j % frst == 0:
            linumbers.append(frst)
            j /= frst
    number.append(linumbers)
    numberswith.append(sorted(list(set(linumbers))))

for i in range(len(number)):
    if len(number[i]) > a:
        a = len(number[i])
        numa = numbers[i]
    if len(numberswith[i]) > b:
        b = len(numberswith[i])
        numb = numbers[i]
print(numa, a)
print(numb, b)