class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        no_dupes = set()
        index = 0
        for num in nums:
            if not num in no_dupes:
                no_dupes.add(num)
                nums[index] = num
                index+=1
    
        return len(no_dupes)
