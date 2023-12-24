# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while right - left > 1 and isBadVersion(right):
            mid = (right + left) // 2
            check = isBadVersion(mid)
            print(left, mid, right, check)
            if check:
                right = mid
            else:
                left = mid
        return right