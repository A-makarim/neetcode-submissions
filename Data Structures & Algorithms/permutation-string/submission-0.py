class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1 = len(s1)
        l = 0
        r = lens1 -1
        print(l,r)
        print(len(s2))
        
        while r < len(s2):
            s1copy = list(s1)
            substring= s2[l:r+1]

            # NOW CHECK IF IT IS IN S1
            for i in substring:
                if i in s1copy:
                    s1copy.remove(i)
                    
                if len(s1copy) == 0:
                    return True

                    
                
            l +=1
            r +=1
            print(l,r)

        return False

        