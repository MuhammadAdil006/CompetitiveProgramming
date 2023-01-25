cases = int(input().rstrip())
ans = []
inp = []
for i in range(cases):
    a = list(map(int, input().rstrip().split(' ')))
    inp.append(a)


def solve(a):
    b = 0
    if a[1] > a[0]:
        b += 1
    if a[2] > a[0]:
        b += 1
    if a[3] > a[0]:
        b += 1
    return b


for i in range(cases):
    print(solve(inp[i]))
