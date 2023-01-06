cases = int(input().rstrip())
inp = []
for i in range(cases):
    _ = input().rstrip()
    inp.append(input().rstrip())


def solve(a):
    dic = {}
    dic['T'] = False
    dic['i'] = False
    dic['m'] = False
    dic['u'] = False
    dic['r'] = False

    if len(a) != 5:
        return "NO"
    else:
        for i in a:
            if i in dic.keys():
                dic[i] = True
            else:
                return "NO"
    if False in dic.values():
        return "NO"
    else:
        return "YES"


for i in range(cases):
    print(solve(inp[i]))
