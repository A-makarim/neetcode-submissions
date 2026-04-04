class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        m = {}
        c = set(s)
        maxx = 0
        for i in range(len(s)): 
            m[s[i]] = 1 + m.get( s[i] , 0)  # increament counts

            while (i - left +1) - max(m.values()) >k:
                m[s[left]] -=1
                left+=1

            maxx = max(maxx,i - left +1 )
        return maxx




        

         