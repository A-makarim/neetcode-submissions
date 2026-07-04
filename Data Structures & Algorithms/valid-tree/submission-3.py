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

        print(mapp)
        allow = True

        # now we have a adjacency list
        # for zero, values give all nodes zero is connected to  
        # now visit a node, if cyclic, return false
        # keep track of visited node. if comes again in visited, False

        def dfs(n, parent):
            nonlocal visited,num,allow
            if n in visited:
                return False

            print(visited)
            num +=1
            visited.append(n)
            for i in mapp[n]:   # get all the nodes its connected to
                if i == parent:
                    continue

                x = dfs(i, n)     # dfs all the child nodes
                if x == False:
                    break
            return True

        if not dfs(0,-1):
            return False
        return len(visited) ==n