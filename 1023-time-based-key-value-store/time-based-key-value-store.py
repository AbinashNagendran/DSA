class TimeMap:

    def __init__(self):
        self.timemap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([timestamp, value])        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        items = self.timemap[key]
        left = 0
        right = len(items) - 1
        ans = ""
        while left <= right:
            index = (left+right) // 2
            if items[index][0] <= timestamp:
                ans =  items[index][1]
                left = index + 1
            else: 
                right = index - 1 
        return ans





        
        
