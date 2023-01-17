def permutation(a, i=0):
    if i == len(a):
        return a
    ans = []
    for j in range(i, len(a)):
        word = [c for c in a]
        # swapping the word
        word[i], word[j] = word[j], word[i]
        ans.extend(permutation(word, i+1))
    return ans


def solve(a, length):
    print(a)
    count = 0
    ans = []
    while (True):
        if count >= len(a):
            break
        ans.append(a[count:count+length])
        count += length
    return ans


print(solve(permutation([1, 2, 3]), 3))

#built in 
from itertools import permutations


def perm(a):
    return list(permutations(a, len(a)))


for i in perm([1, 2, 3]):
    print(list(i))
