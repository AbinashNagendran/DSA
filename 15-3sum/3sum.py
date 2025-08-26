class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =  []
        for i, a in enumerate(nums):
            # if our first number is positive, no way to make a sum
            if a > 0:
                break
            # skip over dups
            if i > 0 and a == nums[i- 1]:
                continue

            start = i + 1
            end = len(nums) - 1
            while start < end: 
                three_sum = nums[start] + nums[end] + a
                if three_sum > 0:
                    end-=1
                elif three_sum < 0:
                    start+=1
                else:
                    res.append([nums[start], nums[end], a])
                    start+=1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start+=1
        return res



            

            

            
                
                    
        