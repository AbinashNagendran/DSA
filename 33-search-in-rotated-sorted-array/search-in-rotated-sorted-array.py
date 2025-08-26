class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            index = (left + right) // 2
            if nums[index] == target:
                return index
            if nums[left] <= nums[index]:
                if nums[left] <= target and target < nums[index]:
                    right = index - 1
                else:
                    left = index + 1
            else:
                if nums[right] >= target and target > nums[index]:
                    left = index + 1
                else:
                    right = index - 1
        return -1