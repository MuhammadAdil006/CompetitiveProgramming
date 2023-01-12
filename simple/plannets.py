cases = int(input().rstrip())
c = []
inp = []
for i in range(cases):
    a = list(map(int, input().rstrip().split(' ')))
    c.append(a[1])
    inp.append(list(map(int, input().rstrip().split(' '))))


def solve(inp, c):
    cost = 0
    dic = {}
    for i in inp:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    for key, val in dic.items():
        cost += min(val, c)

    return cost


for i in range(cases):
    print(solve(inp[i], c[i]))
