cases = int(input().rstrip())
inp = []
for I in range(cases):
    inp.append(int(input().rstrip()))


def solve(m):
    return m - 10**(len(str(m)) - 1)


for J in range(cases):
    print(solve(inp[J]))
