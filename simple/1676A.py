cases = int(input().rstrip())
ans = []
inp = []
for i in range(cases):
    a = input().rstrip()
    inp.append(a)


def solve(a):
    sum1 = 0
    sum2 = 0
    for i in range(0, 3):
        sum1 += int(a[i])
    for i in range(3, 6):
        sum2 += int(a[i])
    if sum1 == sum2:
        return 'Yes'
    return 'No'


for i in range(cases):
    print(solve(inp[i]))
