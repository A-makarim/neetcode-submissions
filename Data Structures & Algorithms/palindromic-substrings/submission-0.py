class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0 
        totallen = len(s)

        def expand(l , r):
            total = 0 
            while l >= 0 and r < totallen and s[l] == s[r]:
                total += 1
                l -=1
                r +=1
            return total

        for i in range(len(s)):
            count += expand(i, i) #even cases
            count += expand(i, i+1) #odd cases
            
        return count
