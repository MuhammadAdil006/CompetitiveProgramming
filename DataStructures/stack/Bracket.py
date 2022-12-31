from collections import deque

 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) != 0:
                    if i == ')' and stack[-1] == '(':
                        stack.pop()
                    elif i == '}' and stack[-1] == '{':
                        stack.pop()
                    elif i == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
