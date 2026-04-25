class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # you have nums. wow. give kth largest? heap will giv eyou smallest.
        # keep poppppping until you are k length

        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]
        