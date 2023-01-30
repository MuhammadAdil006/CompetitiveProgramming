t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    cnt = 0
    for p in range((n//2), -1, -1):
        if s[p] == s[n//2]:
            cnt += 1
        else:
            break
    for p in range((n//2)+1, n):
        if s[p] == s[n//2]:
            cnt += 1
        else:
            break
    print(cnt)
