class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while n:
            s = str(n)
            temp = 0
            for m in s:
                temp += int(m) ** 2
            n = temp
            if n == 1:
                return True
            elif n in d:
                return False
            else:
                d[n] = None
        return False