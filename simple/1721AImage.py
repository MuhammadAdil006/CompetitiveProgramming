cases = int(input().rstrip())
ans = []
inp = []
for i in range(cases):
    a = input().rstrip()
    b = input().rstrip()
    inp.append(a+b)


def solve(a):
    li = [i for i in a]
    lis = set(li)
    return len(lis)-1


for i in range(cases):
    print(solve(inp[i]))
