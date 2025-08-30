class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []

        minHeap = []

        for i in range(len(points)):
            dist = math.sqrt(math.pow(points[i][0] - 0, 2) + math.pow(points[i][1] - 0, 2))
            minHeap.append((dist, points[i]))


        heapq.heapify(minHeap)

        for i in range(k):
            ans.append(heapq.heappop(minHeap)[1])
        return ans
        