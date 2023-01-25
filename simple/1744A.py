cases = int(input().rstrip())
ans = []
inp = []
string = []
for i in range(cases):
    _ = input().rstrip()
    a = list(map(int, input().rstrip().split(' ')))
    stri = input().rstrip()
    inp.append(a)
    string.append(stri)


def solve(a, b):
    dic = {}
    for i in range(len(a)):
        if dic.get(a[i]) is None:
            dic[a[i]] = b[i]
    c = ""
    for i in a:
        c += dic[i]
    if b == c:
        return "YES"
    return "NO"


for i in range(cases):
    print(solve(inp[i], string[i]))
