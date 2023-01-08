cases = int(input().rstrip())
inp = []
for i in range(cases):
    _ = input().rstrip()
    inp.append(list(map(int, input().rstrip().split(' '))))


def solve(a):
    mem = {}
    ele = 0
    for i in range(len(a)):
        preXor = 0
        for j in range(0, i):
            preXor = preXor ^ a[j]
        postXor = 0
        for j in range(i+1, len(a)):
            postXor = postXor ^ a[j]
        if preXor ^ postXor == a[i]:
            ele = a[i]
            break

    return ele


for i in range(cases):
    print(solve(inp[i]))
