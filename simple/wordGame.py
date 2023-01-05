cases = int(input().rstrip())
inp1 = []
inp2 = []
inp3 = []
for i in range(cases):
    _ = input().rstrip()
    inp1.append(input().rstrip().split(' '))
    inp2.append(input().rstrip().split(' '))
    inp3.append(input().rstrip().split(' '))


def solve(a, b, c):
    dic1 = {}
    dic2 = {}
    dic3 = {}
    for i in a:
        dic1[i] = True
    for i in b:
        dic2[i] = True
    for i in c:
        dic3[i] = True
    p1, p2, p3 = 0, 0, 0
    for i in a:
        if i in dic3.keys() and i in dic2.keys():
            # do nothing
            p1 += 0
        elif i in dic3.keys() or i in dic2.keys():
            p1 += 1
        else:
            p1 += 3
    for i in b:
        if i in dic1.keys() and i in dic3.keys():
            # do nothing
            p2 += 0
        elif i in dic3.keys() or i in dic1.keys():
            p2 += 1
        else:
            p2 += 3
    for i in c:
        if i in dic1.keys() and i in dic2.keys():
            # do nothing
            p3 += 0
        elif i in dic1.keys() or i in dic2.keys():
            p3 += 1
        else:
            p3 += 3
    return str(p1)+' '+str(p2)+' '+str(p3)


for i in range(cases):
    print(solve(inp1[i], inp2[i], inp3[i]))
