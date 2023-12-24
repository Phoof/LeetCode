class Solution:
    def countBits(self, n: int) -> List[int]:
        d = {0:0}
        def reduceNum(n):
            if n in d:
                return d[n]
            elif (n & 1 == 1):
                d[n] = 1 + reduceNum(n >> 1)
                d[n - 1] = reduceNum(n - 1)
            else:
                d[n] = reduceNum(n >> 1)
                d[n - 1] = reduceNum(n - 1)
            return d[n]
        reduceNum(n)
        d = dict(sorted(d.items())) 
        return d.values()