class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-s for s in stones]
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            x, y = -heapq.heappop(minHeap), -heapq.heappop(minHeap)
            new = abs(x-y)
            if new != 0:
                heapq.heappush(minHeap, -new)
        return -minHeap[0] if minHeap else 0