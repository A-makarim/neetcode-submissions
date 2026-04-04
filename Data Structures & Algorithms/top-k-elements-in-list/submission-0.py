class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i,n in enumerate(nums):
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1


        sortt = sorted(d.items(), key = lambda x : x[1], reverse = True)
        l =[]
        for i in range(k):
            l.append (sortt[k-i-1][0])

        return l
        


       