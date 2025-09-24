class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # break up 2 cases, when last digits is 9 or not
        if digits[-1] != 9:
            digits[-1]+=1
            return digits
        else:
            pointer = len(digits) - 1
            while pointer >=0 and digits[pointer] == 9:
                pointer-=1
            # pointer digit after seeing 9's

            if pointer >=0:
                digits[pointer]+=1
                for i in range(pointer + 1, len(digits)):
                    digits[i] = 0
            
            else:
                # insert a new digit
                digits = [1] + digits
                for i in range(1, len(digits)):
                     digits[i] = 0
            return digits




        