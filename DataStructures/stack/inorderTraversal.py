
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> list:
    stack = deque()
    lis = []
    while (True):
        if root is not None:
            stack.append(root)
            root = root.left
        elif stack:
            root = stack.pop()
            lis.append(root.val)
            root = root.right
        else:
            break
    return lis
