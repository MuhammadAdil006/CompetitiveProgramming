# cases = int(input().rstrip())
# ans = []
# inp = []


# def solve(a, l, r):
#     b = a[l:r]
#     print("arr", b)
#     if l>r:
#         return l-1,r

#     ans = r-l-len(list(set(b)))
#     ans2 = r-l-solve(b, l+1, r)
#     ans3 = r-l-solve(b, l, r-1)
#     if ans > ans2 and ans > ans3:
#         return l+1, r
#     elif ans2 > ans and ans2 > ans3:
#         return l+1, r-1
#     else:
#         return l+1, r-1


# for i in range(cases):
#     _ = int(input().rstrip())
#     inp.append(list(map(int, input().rstrip().split(' '))))
# for i in range(cases):
#     print(inp[i])
#     print(solve(inp[i], 0, len(inp[i])))
