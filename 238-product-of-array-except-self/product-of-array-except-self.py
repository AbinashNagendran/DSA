

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [] 
        length = len(nums)
        prefix_product = []
        suffix_product = []
        product_foward = 1
        product_backwards = 1
        for i in range(length):
            product_foward = product_foward * nums[i]
            prefix_product.append(product_foward)

            product_backwards = product_backwards * nums[length - 1 - i]
            suffix_product.append(product_backwards)
        for i in range(length):
            if i == 0:
                ans.append(suffix_product[length - 2])
            elif i == length - 1:
                ans.append(prefix_product[i-1])

            else:
                left_side_number = prefix_product[i - 1]
                right_side_number = suffix_product[length - 1 - i - 1]
                ans.append(left_side_number*right_side_number)

        return ans



        
       



        