class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in match:
                if not stack or stack.pop() != match[char]:
                    return False
            else:
                stack.append(char)

        return not stack