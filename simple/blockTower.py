cases = int(input().rstrip())
inp = []
for i in range(cases):
    _ = input().rstrip()
    inp.append(list(map(int, input().rstrip().split(' '))))


def solve(a):
    for i in range(1, len(a)):
        while a[i] > a[0]:
            if (a[i] % 2 == 0 and a[0] % 2 == 0) or ((a[i] % 2 != 0 and a[0] % 2 != 0)):
                val = (a[i]-a[0])//2
                a[i] = a[i]-val
                a[0] += val
            else:
                val = (a[i]-a[0])//2
                if val >= 1:
                    a[i] -= (val+1)
                    a[0] += (val+1)
                elif val == 0:
                    a[i] -= 1
                    a[0] += 1

    return a[0]


for i in range(cases):
    e = inp[i]
    d = e[1:]
    d = sorted(d, reverse=False)
    d.insert(0, e[0])
    # e.insert(0, inp[0])
    print(solve(d))
