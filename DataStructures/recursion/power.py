class Solution:
    def myPow(self, x: float, n: int) -> float:
        def r(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n % 2 == 0:
                a = r(x, n/2)
                return a*a
            else:
                a = r(x, n//2)
                return a*a*x
        if n >= 0:
            return r(x, n)
        else:
            return (1/r(x, -1*n))
