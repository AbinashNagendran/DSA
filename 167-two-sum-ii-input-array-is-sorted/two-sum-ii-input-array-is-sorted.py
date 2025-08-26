class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
    

        for i in range(len(numbers)):
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            if sum > target:
                right = right - 1
            else: 
                left = left + 1
        
        