class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        

        res = []
        sublist = [] 
        final = []
        last = None

        def dfs(openn, closee):

            if len(sublist) == 2*n:
                res.append(list(sublist))
                return

            if openn < n:
            
                sublist.append("(")
                dfs(openn+1, closee)  # call again and append a ( or ) . until len is 2*n. 
                sublist.pop()

            if closee < openn:
                sublist.append(")")
                dfs(openn, closee+1)
                sublist.pop()

        
        dfs(0,0)

        for i in res:
            result = ''.join(i)
            final.append(result)
        
        return final
            

        
    


        
        
