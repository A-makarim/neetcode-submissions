class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #first we need to map these
        mapping = {"2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl", 
        "6": "mno", 
        "7": "pqrs", 
        "8": "tuv",
        "9": "wxyz"}

        res = []
        parts = []

        def dfs(c,i):
            if len(parts) == len(digits):
                res.append("".join(parts))
                return 
            for j in mapping[digits[i]]:
                parts.append(j)
                dfs(c, i+1)
                parts.pop()
        
        dfs("", 0)
        if len(digits) == 0:
            return []
        return res



        
        