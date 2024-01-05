class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        tab = [0, 0, 1]

        while n > 1:
            tab[0] = tab[1]
            tab[1] = tab[2]
            tab[2] = tab[0] + tab[1]
            n -= 1
        
        return tab[2]