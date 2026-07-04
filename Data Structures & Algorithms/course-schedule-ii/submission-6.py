class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {}
        for i in prerequisites:
            if i[0] in premap:
                premap[i[0]].append(i[1])
            else: 
                premap[i[0]] = [i[1]]
        taken = []
        totake = []
        x = True
        order = []
        print(premap)

        def dfs(n):
            nonlocal totake, taken, x, order
            if n in taken:
                return True
            if n not in premap.keys():
                if n not in taken:
                    taken.append(n)
                    order.append(n)
                return True
            if n in premap.keys():
                for i in premap[n]: #1
                    if i in totake:
                        return False
                    totake.append(i)  # have to take 0
                    x = dfs(i)   # 0 will get appended again
                    if x == False:
                        break
                    totake.remove(i)
                    taken.append(i)
                    taken.append(n)
                    order.append(n)

            return x

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order
        