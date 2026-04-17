class Solution:
    def isValid(self, s: str) -> bool:
        parens = {")":"(", "}":"{", "]":"["}
        stack = []

        for i in range(len(s)):
            if s[i] in parens.keys():
                if stack and stack[-1] == parens[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
            
        if not stack:
            return True
        else:
            return False