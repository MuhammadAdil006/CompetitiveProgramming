cases = int(input().rstrip())
ans = []
inp = []
for i in range(cases):
    stri = int(input().rstrip())
    inp.append(stri)


def solve(a):
    lis = [a//3, a//3, a//3]
    x = a % 3
    if x == 0:
        lis[2] -= 1
        lis[1] += 1
    elif x == 1:
        lis[1] += 2
        lis[2] -= 1
    else:
        lis[1] += 2
        lis[2] -= 1
        lis[0] += 1
    return lis


for i in range(cases):
    a = solve(inp[i])
    print(a[0], " ", a[1], " ", a[2])
