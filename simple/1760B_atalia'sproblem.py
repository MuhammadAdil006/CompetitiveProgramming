

def initialize():
    dic = {}
    i = "a"
    dic[i] = 1
    for j in range(2, 27):
        i = chr(ord(i)+1)
        dic[i] = j
    return dic


def solve2(a, b):
    ans = 1
    for i in b:
        ans = max(ans, a[i])
    return ans


def solve():
    dic = initialize()
    cases = int(input().rstrip())
    inp = []
    for i in range(cases):
        _ = input().rstrip()
        inp.append(input().rstrip())
    for i in range(cases):
        print(solve2(dic, inp[i]))


if __name__ == "__main__":
    solve()
