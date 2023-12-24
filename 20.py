class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = ")}]"
        pairs = {"(": ")", "{": "}", "[": "]"}
        for b in s:
            if b in closers:
                if not stack:
                    return False
                elif pairs[stack[-1]] == b:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        if not stack:
            return True
        return False