class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = 0
        r = 0
        counts = {}
        for i, a in enumerate(s):
            counts[a] = i
        lens = []
        
        print(counts)

        for i, a in enumerate(s):
            r = max(r, counts[a])
            if i == r:
                lens.append(r - l + 1)
                l = r + 1

        
        return lens

        