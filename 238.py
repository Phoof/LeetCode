class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        prod1 = 1
        for i in range(len(nums)):
            arr[i] =  prod1
            prod1 *= nums[i]
        prod2 = 1
        for j in range(len(nums) - 1, -1, -1):
            arr[j] *= prod2
            prod2 *= nums[j]
        return arr