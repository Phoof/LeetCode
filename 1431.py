class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        largest = max(candies)
        for candy in candies:
            if candy + extraCandies >= largest:
                ans.append(True)
            else:
                ans.append(False)
        return ans