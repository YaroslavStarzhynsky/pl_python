def balance(text, brackets ="()[]"):
    op,cl = brackets[::2],brackets[1::2]
    stack = []
    for i in text:
        if i in op:
            stack.append(op.index(i))
        elif i in cl:
            if stack and stack[-1] == cl.index(i):
                stack.pop()
            else:
                return False
    return (not stack)
n = int(input())
a = []
i = 0
while i < n:
    x = input()
    if x:
        a.append(x)
    else:
        break
k = 0
while k < n:
    if(balance(str(a[k]))):
        print("Yes")
    else:
        print("No")
    k+=1


