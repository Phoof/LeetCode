class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            s = str(num)
            temp = 0
            for n in s:
                temp += int(n)
            num = temp
            if len(str(num)) == 1:
                return num