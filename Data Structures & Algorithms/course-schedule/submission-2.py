class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {}
        for i in prerequisites:
            if i[0] in premap:
                premap[i[0]].append(i[1])
            else: 
                premap[i[0]] = [i[1]]
        taken = []
        totake = []
        x = True
        print(premap)

        def dfs(n):
            nonlocal totake, taken, x
            if n not in premap.keys():
                taken.append(n)
                return True
            if n in premap.keys():
                for i in premap[n]:
                    if i in totake:
                        return False
                    totake.append(i)
                    x = dfs(i)
                    if x == False:
                        break
                    totake.remove(i)
                    taken.append(i)

            return x

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True




            


            # else that course in already taken


        