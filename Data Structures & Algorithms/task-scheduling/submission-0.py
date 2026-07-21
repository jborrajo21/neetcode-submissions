from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = 0
        seen = {}
        maxHeap = []

        for task in tasks:
            seen[task] = seen.get(task, 0) + 1
        for task in seen:
            maxHeap.append(-seen[task])
        heapq.heapify(maxHeap)
        
        q = deque()
        while maxHeap or q:
            counter +=1

            if not maxHeap:
                counter = q[0][1]
            else:
                freq = 1 + heapq.heappop(maxHeap)
                if freq:
                    q.append((freq, counter + n))
            if q and q[0][1] == counter:
                heapq.heappush(maxHeap, q.popleft()[0])
        return counter