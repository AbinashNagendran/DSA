class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        multiplier = 1
        s = s.strip()
        start_index = 0
        if not s:
            return 0
        if s[0] == "-":
            multiplier = -1
            start_index = 1
        elif s[0] == "+":
            start_index = 1
        
        while start_index < len(s) and s[start_index] == "0" :
            start_index+=1
        if start_index == len(s):
            return 0

        end_index = start_index
        while end_index < len(s) and s[end_index].isdigit():
            end_index+=1
        
        ans = int(s[start_index: end_index]) * multiplier if end_index != start_index else 0
        if ans < -2147483648:
            return -2147483648 
        if ans > 2147483647:
            return 2147483647
        return ans



        