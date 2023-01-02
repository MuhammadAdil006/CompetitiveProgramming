cases = int(input().rstrip())
ans = []
for i in range(cases):
    a = list(map(int, (input().rstrip().split(' '))))
    a = sorted(a)
    ans.append(a[1])
for i in range(cases):
    print(ans[i])
