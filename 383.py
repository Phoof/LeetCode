class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = {}
        d2 = {}
        for x in ransomNote:
            d1[x] = d1.get(x, 0) + 1
        for y in magazine:
            d2[y] = d2.get(y, 0) + 1
        for x in d1:
            if not (x in d2 and d1[x] <= d2[x]):
                return False
        return True