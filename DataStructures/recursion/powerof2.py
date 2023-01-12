class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        def recurse(a, n):
            if pow(2, a) > n:
                return False
            elif pow(2, a) == n:
                return True
            else:
                return recurse(a+1, n)
        return recurse(1, n)
