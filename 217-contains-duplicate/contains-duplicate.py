class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums=set()
        for number in nums:
            if number in unique_nums:
                return True
            unique_nums.add(number)
            
        return False
        