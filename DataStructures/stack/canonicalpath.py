from collections import deque


def solve(s):
    stack = deque()
    i = 0
    c = (s.split("/"))
    print(c)
    e = []
    for i in c:
        if i != '' and i != '.':
            e.append(i)
    print(e)
    for i in e:
        if i == ".." and len(stack) != 0:
            stack.pop()
        else:
            if i != "..":
                stack.append(i)
    print(stack)
    res = "/"
    for i in stack:
        res = res+i+"/"
    if len(res) > 1 and res[-1] == "/":
        return res[:-1]
    return res


print(solve("/../"))
