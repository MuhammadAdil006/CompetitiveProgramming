import sys


def maxSubArray(num, i, j):
    if dic.get((i, j)) is None:

        if i == j:
            dic[(i, j)] = num[i]
            return dic[(i, j)]
        else:
            Total_sum = sum(num[i: j+1])
            if dic.get((i+1, j)) is None:
                dic[(i+1, j)] = maxSubArray(num, i+1, j)
            if dic.get((i, j-1)) is None:
                dic[(i, j-1)] = maxSubArray(num, i, j-1)

            dic[(i, j)] = max(Total_sum, dic[(i+1, j)], dic[(i, j-1)])
            return dic[(i, j)]
    else:
        return dic[(i, j)]


dic = {}
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4], 0, 8))
