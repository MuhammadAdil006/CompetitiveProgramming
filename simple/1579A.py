cases = int(input().rstrip())
ans = []
inp = []
for i in range(cases):
    stri = input().rstrip()
    inp.append(stri)


def solve(a):
    dic = {'A': 0, 'B': 0, 'C': 0}
    for i in a:
        dic[i] += 1
    if dic['B']-dic['A'] >= 0:
        dic['B'] = dic['B']-dic['A']
        if dic['C']-dic['B'] == 0:
            return "Yes"
        return "No"
    else:
        return "No"


for i in range(cases):
    print(solve(inp[i]))
