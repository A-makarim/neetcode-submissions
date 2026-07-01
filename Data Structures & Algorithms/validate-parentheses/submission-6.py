class Solution:
    def isValid(self, s: str) -> bool:
        match = {')':'(', ']':'[', '}':'{'}   

        stack = []  

        for char in s:
            if char in match.values():
                stack.append(char)           # ad opening bracket

            else:                                # if not opening bracket
                if not stack:                    # if you encounter a closing bracket before
                    return False
                if stack.pop() != match[char]:   # you need a closing bracket for last element in stack
                    return False

        return len(stack) == 0              #at one point you will have removed all opening brackets 
