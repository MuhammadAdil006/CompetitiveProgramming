cases = int(input().rstrip())
ans = []
inp = []
for i in range(cases):
    _ = input().rstrip()
    a = list(map(int, input().rstrip().split(' ')))
    inp.append(a)


def solve(a):
    return max(a)-min(a)


for i in range(cases):
    print(solve(inp[i]))
