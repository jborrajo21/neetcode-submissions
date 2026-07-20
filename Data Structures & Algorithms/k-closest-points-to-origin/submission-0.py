from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(coords):
            return sqrt(coords[0]**2 + coords[1]**2)
        
        minHeap = [(-distance(p), p) for p in points]
        heapq.heapify(minHeap)
        
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        res = []
        for p in minHeap:
            res.append(p[1])
        return res