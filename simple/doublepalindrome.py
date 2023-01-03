cases = int(input().rstrip())
inp = []
for i in range(cases):
    inp.append(input().rstrip())


def doubling(a):
    b = ""
    for i in a:
        b += i*2

    return b


def checkP(a):
    if len(a) == 0:
        return True
    c = a[::-1]
    if a == c:
        return True
    return False


def makePalindrome(a):
    b = ""
    while (not checkP(a)):
        b += a[0]
        a = a[2:]
    c = b[::-1]
    b += a+c
    return b


for i in range(cases):
    dugna = doubling(inp[i])
    print(makePalindrome(dugna))
