class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = curr = 0
        while curr < target:
            if right == len(nums):
                return 0
            curr += nums[right]
            right += 1
        ans = right
        for i in range(right, len(nums)):
            curr += nums[right]
            right += 1
            while curr >= target:
                curr -= nums[left]
                left += 1       
                if curr >= target:
                    ans = min(ans, right - left)
        while curr >= target:
            curr -= nums[left]
            left += 1       
            if curr >= target:
                ans = min(ans, right - left)
        return ans