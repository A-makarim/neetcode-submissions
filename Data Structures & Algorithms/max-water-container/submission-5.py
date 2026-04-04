class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0            
        left =0
        right = len(heights) - 1 

        for i, n in enumerate(heights[:len(heights)-1]):
            w =  right - left
            if left <= right: 
                h = min(heights[left], heights[right])
                a = h * w
                #print(i , "-"*50)
                m = max(m, a)
                print(heights)
                print(" "*((i*3)),heights[left],(" "), heights[right], "w=", w , "a=",  a )
            
                if heights[left] < heights[right]:
                    left += 1
                else:
                    right -= 1

            
        return m


                
                

        