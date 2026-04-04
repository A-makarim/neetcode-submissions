class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxx = 0
        while left <= len(s)-1 and right <= len(s) -1 :
            if len(s[left:right+1]) == len(set(s[left:right+1])):
                right += 1
            else: 
                left += 1

            maxx = max(maxx, right - left)
        return maxx