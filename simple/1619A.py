cases = int(input().rstrip())
ans = []
inp = []
for i in range(cases):
    a = input().rstrip()
    inp.append(a)


def solve(a):
    if len(a) % 2 == 0:
        i = len(a)
        str1 = a[0:i//2]
        str2 = a[i//2:]
        if str1 == str2:
            return "Yes"
        return "No"
    else:
        return "No"


for i in range(cases):
    print(solve(inp[i]))
