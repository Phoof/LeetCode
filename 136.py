class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for el in nums:
            d[el] = d.get(el, 0) + 1
        for el, val in d.items():
            if val == 1:
                return el
            
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for el in nums:
            d[el] = d.get(el, 0) + 1
        return min(d, key=d.get)