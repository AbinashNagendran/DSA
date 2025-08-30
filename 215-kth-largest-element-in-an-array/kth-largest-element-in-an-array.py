class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums) # O(N)

        ans = -heapq.heappop(nums)
        for i in range(k - 1):
            ans = -heapq.heappop(nums)
        return ans
        