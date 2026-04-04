from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = Counter(s)
        set2 = Counter(t)
        if set1 == set2:
            return True
        else:
            return False

        