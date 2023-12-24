class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1
        return max(d, key=d.get)