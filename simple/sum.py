cases = int(input().rstrip())
ans = []
inp = []
for i in range(cases):
    li = list(map(int, input().rstrip().split(' ')))
    inp.append(li)


def solve(a, b):
    if b == 3:
        return "NO"
    if a[0]+a[1] == a[2]:
        return "YES"
    else:
        last = a.pop()
        a.insert(0, last)
        b += 1
        return solve(a, b)


for i in range(cases):
    print(solve(inp[i], 0))
