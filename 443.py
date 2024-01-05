class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        curr = ""
        count = 1
        for c in chars:
            if c != curr:
                ans.append(curr)
                if count > 1:
                    for n in str(count):
                        ans.append(n)
                curr = c
                count = 1
            else:
                count += 1
        ans.append(curr)
        if count > 1:
            for n in str(count):
                        ans.append(n)
        ans = ans[1:]
        for i in range(len(ans)):
            chars[i] = ans[i]
        return len(ans)

class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        i = 0
        while i < len(chars):
            letter = chars[i]
            count = 0
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
            chars[ans] = letter
            ans += 1
            if count > 1:
                for n in str(count):
                    chars[ans] = n
                    ans += 1
        
        return ans