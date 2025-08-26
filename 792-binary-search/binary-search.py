class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left <= right):
            index = int((right + left) / 2)
            num = nums[index]
            if num == target:
                return index
            if num < target:
                left = index + 1
            else:
                right = index - 1

        return -1
        