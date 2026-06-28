class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = [] #final
        parts = []

        def ispal(s, i , j):
            i = 0
            j = len(s)-1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i +=1
                j-=1
            return True 


        def dfs(i):
            if i>= len(s): ## we have reached the end of the word iteration
                res.append(list(parts))
                return

            for j in range(i, len(s)):    # 0 01 012 0123 so all starting from zero
                if ispal(s[i: j+1], i , j):
                    parts.append(s[i:j+1])
                    dfs(j+1)                   # 1 12  123 1234. second itr # 2 23 234 2345
                    parts.pop()

        dfs(0)
        return res

            
