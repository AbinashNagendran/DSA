class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        symbols = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            if i != len(s) - 1 and symbols[s[i+1]] > symbols[s[i]]:
                    count-=symbols[s[i]]  
            else:
                count+=symbols[s[i]]

            
        return count

