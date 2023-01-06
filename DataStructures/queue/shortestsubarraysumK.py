from collections import deque
import sys


def shortestLength(li, k):
    mem = [[0 for i in range(len(li))] for z in range(len(li))]

    length = sys.maxsize
    flag = False
    for i in range(len(li)):
        queue = deque()
        for j in range(i, len(li)):
            queue.append(li[j])
            if mem[i][j] != 0:
                summation = mem[i][j]
            else:
                summation = sum(queue)
                mem[i][j] = summation
            if summation >= k:
                flag = True
                length = min(length, len(queue))
    if flag:
        return length
    else:
        return -1


print(shortestLength([1, 2], 4))
