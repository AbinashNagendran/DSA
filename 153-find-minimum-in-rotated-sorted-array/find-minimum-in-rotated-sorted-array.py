class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            index = int((right + left) / 2)
            num = nums[index]
            right_num = nums[right]
            if num > right_num:
                left = index + 1
            else:
                right = index
        return nums[left]