cases = int(input().rstrip())
ans = []
inp = []
keys = []
for i in range(cases):
    keys.append(int(input().rstrip()))
    li = list(map(int, input().rstrip().split(' ')))
    inp.append(li)


def solve(a, keys):
    count = 0
    for i in range(3):
        keys = keys-1
        if keys > -1:
            count += 1
            keys = a[keys]
        else:
            break
    if count >= 3:
        return "YES"
    return "NO"


for i in range(cases):
    print(solve(inp[i], keys[i]))
