cases = int(input().rstrip())
ans = []
inp = []
for i in range(cases):
    _ = input().rstrip()
    a = list(map(int, input().rstrip().split(' ')))
    inp.append(a)


def solve(a):
    dic = {}
    for i in a:
        if dic.get(i) is not None:
            dic[i] += 1
        else:
            dic[i] = 1
    for key, values in dic.items():
        if values % 2 == 0:
            if values != 0:
                dic[key] = 2
        else:
            dic[key] = 1
    summ = 0
    twos = []
    for i, _ in dic.items():
        if dic[i] == 2:
            twos.append(2)
        else:
            summ += 1
    if len(twos) % 2 == 0:
        summ += sum(twos)//2
    else:
        summ += sum(twos[:len(twos)-1])//2
    return summ


for i in range(cases):
    print(solve(inp[i]))
