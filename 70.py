class Solution:
    def climbStairs(self, n: int) -> int:
        d = {1:1, 2:2}
        def fib(n):
            if n in d:
                return d[n]
            d[n] = fib(n - 2) + fib(n - 1)
            return d[n] 
        return fib(n)