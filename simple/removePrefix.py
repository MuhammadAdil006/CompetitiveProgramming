t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    s = set()
    res = 0
    for i in range(n-1, -1, -1):
        if a[i] in s:
            res = i + 1
            break
        s.add(a[i])

    ans.append(res)
for i in range(t):
    print(ans[i])
