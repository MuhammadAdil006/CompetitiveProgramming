cases = int(input().rstrip())
inp = []
for i in range(cases):
    inp.append(input().rstrip())


def solve(a):
    if a.upper() == "YES":
        return "YES"
    return "NO"


for i in range(cases):
    print(solve(inp[i]))
