class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        

        # implement bucket sort


        buckets = [] 
        for i in range(len(nums)):
            buckets.append([])
        for key in dic.keys(): 
            index = dic[key] - 1
            buckets[index].append(key)
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            for num in buckets[i]:
                if len(ans) == k:
                    return ans
                else:
                    ans.append(num)
                if len(ans) == k:
                    return ans