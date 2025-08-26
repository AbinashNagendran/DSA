class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # creating a hash set 
        longest = 0
        for num in num_set:
            if (num + 1) in num_set and (num - 1) not in num_set:
                counter = num
                candiate = 1
                while (counter + 1) in num_set:
                    candiate+=1
                    counter+=1
                if candiate > longest:
                    longest = candiate
        if longest == 0 and len(num_set) >= 1:
            return 1
        return longest
                



            


        

        