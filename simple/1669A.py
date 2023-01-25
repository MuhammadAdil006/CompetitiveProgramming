cases = int(input().rstrip())
ans = []
inp = []
for i in range(cases):
    _ = input().rstrip()
    a = list(map(int, input().rstrip().split(' ')))
    inp.append(a)


def solve(a):
    dic = {}
    value = -1
    for i in a:
        if dic.get(i) is None:
            dic[i] = 1
        else:
            dic[i] += 1
            if dic[i] == 3:
                value = i
                return value
    return value


for i in range(cases):
    print(solve(inp[i]))
