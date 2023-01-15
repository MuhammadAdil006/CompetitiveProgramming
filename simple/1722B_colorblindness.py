cases = int(input().rstrip())
ans = []
inp = []
inp2 = []
for i in range(cases):
    _ = input().rstrip()
    inp.append(input().rstrip())
    inp2.append(input().rstrip())
1


def solve(a, b):
    if (len(a) == 0):
        return "YES"
    if (a[0] == b[0]) or (a[0] == 'B' and b[0] == 'G') or (a[0] == 'G' and b[0] == 'B'):
        return solve(a[1:], b[1:])
    return "NO"


for i in range(cases):
    print(solve(inp[i], inp2[i]))
