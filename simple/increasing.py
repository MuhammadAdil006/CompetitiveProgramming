cases = int(input().rstrip())
inp = []
for i in range(cases):
    _ = int(input().rstrip())
    inp.append(list(map(int, input().rstrip().split(' '))))


def solve(a):
    newList = []
    while a:
        ele = min(a)
        a.remove(ele)
        newList.append(ele)
    unique = set(newList)
    if (len(unique) == len(newList)):
        return "YES"
    else:
        return "NO"


for i in range(cases):
    print(solve(inp[i]))
