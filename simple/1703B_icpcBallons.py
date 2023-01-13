cases = int(input().rstrip())
ans = []
inp = []
for i in range(cases):
    _ = input().rstrip()
    li = input().rstrip()
    inp.append(li)


def solve(a):
    dic = {}
    count = 0
    for i in a:
        if i not in dic.keys():
            dic[i] = 1
            count += 2
        else:
            count += 1
    return count


for i in range(cases):
    print(solve(inp[i]))
