from collections import deque


def trap(height: list[int]) -> int:
    def check(height: list[int]) -> int:
        stack = deque()
        sum = 0
        i = 0
        while i <= len(height):

            if (len(height[i:]) > 1) and height[i] > height[i+1]:
                stack.append(height[i])
            if stack:
                j = i+1
                flag = False
                while True:

                    if j >= len(height):
                        stack.clear()
                        flag = True
                        break
                    if height[j] >= stack[0]:
                        break
                    stack.append(height[j])

                    j += 1
                if (not flag):
                    i = j-1

            if stack:
                while stack:
                    sum += stack[0]-stack.pop()
            i += 1

        return sum
    return (max(check(height), check(height[::-1])))

