class Solution:
    def isPalindrome(self, s: str) -> bool:
        left =  0
        right = len(s) - 1     
        s = s.lower()   
        while left < right:
            if ord(s[left]) < ord('a') or ord(s[left]) > ord('z'):
                if ord(s[left]) < ord('0') or ord(s[left]) > ord('9'):
                    left += 1
                    continue

            if ord(s[right]) < ord('a') or ord(s[right]) > ord('z'):
                if ord(s[left]) < ord('0') or ord(s[left]) > ord('9'):
                    right -= 1
                    continue   
            print(s[left])
            print(s[right])
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True





        