class Solution:
    def isValid(self, s: str) -> bool:
        match = {')':'(', ']':'[', '}':'{'}   

        stack = []  

        for char in s:
            if char in "([{":
                print(match.values())
                stack.append(char)           # ad opening bracket

            else:                                # if not opening bracket
                if not stack:                    # if you encounter a closing bracket before
                    return False
                if stack[-1] != match[char]:   # you need a closing bracket for last element in stack
                    return False
                stack.pop()                      # remove the last one from stack

        return len(stack) == 0              #at one point you will have removed all opening brackets 
