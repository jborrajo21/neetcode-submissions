class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        heap = []
        seen = {}

        for task in tasks:
            seen[task] = seen.get(task, 0) + 1
        for task in seen:
            heap.append(-seen[task])
        heapq.heapify(heap)

        q = deque()
        while q or heap:
            time += 1
            
            if not heap:
                time = q[0][1]
            else:
                freq = 1 + heapq.heappop(heap)
                if freq:
                    q.append((freq, time + n))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time
                

