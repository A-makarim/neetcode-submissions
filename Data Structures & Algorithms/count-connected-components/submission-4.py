class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set() # lookup of 0(1)
        mapp = {}
        count =0
    
        for i in edges:
            if i[0] in mapp:
                mapp[i[0]].append(i[1])
            else:
                mapp[i[0]] = [i[1]]

            if i[1] not in mapp:
                mapp[i[1]] = [i[0]]
            else: # it's  a key
                mapp[i[1]].append(i[0])

        print(mapp)

        def dfs(n, p):
            nonlocal visited, mapp
            if n in visited:
                return
            visited.add(n) 
            
            for i in mapp.get(n, []):   # for all the edges connecting:

                # if i is not p
                dfs(i , n) # 1 with 0 parent
            return visited

        for i in range(n):

            if i not in visited:
                x = dfs(i, -1)
                count +=1
        return count
            
            
            





