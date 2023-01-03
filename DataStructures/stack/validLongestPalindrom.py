from collections import deque


def validLongestP(a):
    stack = deque()
    stack.append(-1)
    ans = 0
    for i in range(len(a)):
        if a[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                ans = max(ans, i-stack[-1])

    return ans
