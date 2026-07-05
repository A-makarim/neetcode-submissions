class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mapp = {}
        visited = set()
        found = False

        
        def dfs(n , p):
            if n in visited: 
                return [n,p]
            visited.add(n)
            for i in mapp.get(n, []):
                if i == p:
                    continue
                print(i)
                
                x = dfs(i, n)
                if x is not None:
                    return x
            return None

        for i in edges:
            if i[0] in mapp:
                mapp[i[0]].append(i[1])
            else:
                mapp[i[0]] = [i[1]]
            if i[1] in mapp:
                mapp[i[1]].append(i[0])
            else:
                mapp[i[1]] = [i[0]]

            y = dfs(i[0], -1)
            if y:
                return y
            visited = set()
        return []          
