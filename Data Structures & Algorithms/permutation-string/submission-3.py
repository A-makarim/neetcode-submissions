from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1 = len(s1)
        l = 0
        r = lens1 -1
        
        hashmap = Counter(s1)
        substring = s2[l:r+1]
        hashmap2 = Counter(substring)

        while r < len(s2):
            finding = True
            for i in hashmap:
                if hashmap[i] != hashmap2[i]:
                    finding = False
                    break
            
            if finding == True:
                return True

            left = s2[l]
            hashmap2[left] -=1
            l+=1
            r+=1
            if r == len(s2):
                break
            print(l, r)
            right = s2[r]
            hashmap2[right] = hashmap2.get(right, 0)
            hashmap2[right] +=1
        return False

        