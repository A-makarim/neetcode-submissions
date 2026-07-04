class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check num or nodes are enough
        # check it's not cycling
        # check every node is connected
        visited = []
        num = 0
        mapp ={}

        if n-1 != len(edges):
            return False

        for i in edges:
            if i[0] not in mapp:
                mapp[i[0]] = [i[1]]
            else: # it's  a key
                mapp[i[0]].append(i[1])

            if i[1] not in mapp:
                mapp[i[1]] = [i[0]]
            else: # it's  a key
                mapp[i[1]].append(i[0])

        # now we have a adjacency list
        # for zero, values give all nodes zero is connected to  
        # now visit a node, if cyclic, return false
        # keep track of visited node. if comes again in visited, False

        def dfs(n):
            nonlocal visited,num
            if n in visited:
                return False

            num +=1
            visited.append(n)
            for i in mapp[n]:   # get all the nodes its connected to
                if i == n: 
                    continue
                x = dfs(i)     # dfs all the child nodes
                if x == False:
                    break
            return True

        return dfs(0)