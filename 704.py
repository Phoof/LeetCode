class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
class Solution:
    def search_recursion(self, nums: List[int], target: int) -> int:
        def bs(nums, target, low, high):
            if high >= low:
                mid = (high + low) // 2
                guess = nums[mid]
                if guess == target:
                    return mid
                elif guess < target:
                    return bs(nums, target, mid + 1, high)
                else:
                    return bs(nums, target, low, mid - 1)
            else:
                return -1
        return bs(nums, target, 0, len(nums) - 1)