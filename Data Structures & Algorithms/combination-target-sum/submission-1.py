class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums is a list on int [2 ,5 6, 9]
        # target is a int 9

        # 2, 
        # 2, not 2
        # 2 , 2 , not
        ans = []
        sublist = []

        def dfs(i):

            if sum(sublist) == target:
                ans.append(list(sublist))
                return 
            if sum(sublist) > target:
                return
            if i >= len(nums):
                return

            sublist.append(nums[i])
            dfs(i)

            sublist.pop()
            dfs(i+1)

        dfs(0 )

        return ans
            
                

        