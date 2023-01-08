from collections import deque
from numbers import Integral
import sys


#memorization but time limit exceeded
# def shortestLength(li, k):
#     dic={}
#     for i in range(len(li)):
#         dic[i,i]=li[i]
#     for i in range(len(li)):
#         for j in range(i+1,len(li)):
#            dic[i,j]=dic[i,j-1]+li[j]
#     maxEle=sys.maxsize
#     F=False

#     for key,a in dic.items():
#         if a>=k:
#             F=True
#             maxEle=min(maxEle,key[1]-key[0]+1)
#     if(F):
#         return maxEle
#     return -1

def shortestLength(arr, x):
    n=len(arr)
    # Initialize current sum and minimum length
    curr_sum = 0
    min_len = sys.maxsize
    F=False
    # Initialize starting and ending indexes
    start = 0
    end = 0
    while (end < n and start<n):
 
        # Keep adding array elements while current
        # sum is smaller than or equal to x
        while (curr_sum <= x and end < n):
            curr_sum += arr[end]
            end += 1
 
        # If current sum becomes greater than x.
        while (curr_sum >= x and start < n):
 
            # Update minimum length if needed
            if (end - start < min_len):
                F=True
                min_len = end - start
 
            # remove starting elements
            curr_sum -= arr[start]
            start += 1
    if F:
        return min_len
    return -1
print(shortestLength([2,-1,2], 3))
