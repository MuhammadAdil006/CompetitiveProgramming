cases = int(input().rstrip())
ans = []
inp = []
for i in range(cases):
    inp1 = []
    for j in range(2):
        a = list(map(int, input().rstrip().split(' ')))
        inp1.append(a)
    inp.append(inp1)


def rotate(a):
    rotated = list(zip(*a[::-1]))
    return rotated


def beautiful(a):
    if a[0][0] < a[0][1] and a[1][0] < a[1][1]:
        if a[0][0] < a[1][0] and a[0][1] < a[1][1]:
            return True
        else:
            return False
    else:
        return False


def solve(a):
    if beautiful(a):
        return "Yes"
    else:
        for I in range(3):
            a = rotate(a)
            if beautiful(a):
                return "Yes"
        return "No"


for i in range(cases):
    print(solve(inp[i]))
