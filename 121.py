class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = ans = 0
        right = 1
        length = len(prices)
        while right != length:
            profit = prices[right] - prices[left]
            if right == length:
                return 0
            if profit <= 0:
                left += 1
                right += 1
            else:
                ans = profit
                break

        while right < length - 1:
            right += 1
            profit = prices[right] - prices[left]
            if profit > ans:
                ans = profit
            if profit <= 0:
                left = right

        return ans