from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for i in t:
            need[i] +=1
        setofneeds = set(need.keys())
        print(setofneeds)
        have = {i:0 for i in t}  # we have list of letters and how many of them we need



        final = ""
        min_len = float("inf")
        print(need, have)
        left = 0
        right = -1
        length = len(s) -1
        if sum(need.values()) > length+1:
            return ""

        while right <= length and left <= length:
            print(self.cal_left(need, have))
            if not self.cal_left(need, have) and right < length : # we still need more letters. we can't shoten our window. increase instead
                print("if")
                right +=1 
                print(left, right, "00000")
                print(s[left:right+1])
                if s[right] in setofneeds: ### update your have dict
                    print("second if")
                    have[s[right]] +=1
                    print("fffffffffff",have)
                else:
                    print("movinggg")
            else:  # moving left cuz true orrrr cant move right
                print("else")
                # we have reached the windo. we can start moving left to right to reduce window
                minimum = s[left:right+1]   # first store min
                print(left, right, "1111")
                print("minimu", minimum)
                if len(minimum) < min_len and self.cal_left(need, have):
                    print("elseif trigger")
                    min_len = len(minimum)
                    final = minimum
                    print("fina", final)
                # ifright cannot move and else if also doesnt trigger
                # it means that

                if s[left] in setofneeds:
                    have[s[left]] -=1
                left +=1   # move left
        print(length, right)
        if len(final) == 100:
            return ""
        else:
            return final
    def cal_left(self, dict1 , dict2):
        # dict 1 is the target 
        for i in dict1.keys():
            if dict1[i] > dict2[i]:      # i is the key  
                return False
            else:
                continue
        print("true")
        return True   # have has equal or more letters which is fine. in which case, more left

        
