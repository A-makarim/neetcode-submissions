from collections import defaultdict



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i,n in enumerate(strs):
            d[tuple(sorted((n)))].append(n)
            
        return (list(d.values()))




            