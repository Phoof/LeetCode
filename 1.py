class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, x in enumerate(nums):
            comp = target - x
            if comp in d:
                return [index, d[comp]]
            else:
                d[x] = index
