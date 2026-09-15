class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(set)
        for u,v,cost in times:
            g[u].add((cost,v))
        
        heap = [k]
        heapq.heapify(heap)

        costTo = [float("inf")] * n
        costTo[k-1] = 0

        while heap:
            node = heapq.heappop(heap)
            for cost, n in g[node]:
                if cost + costTo[node - 1] < costTo[n-1]:
                    heapq.heappush(heap, n)
                    costTo[n-1] = cost + costTo[node - 1]
        
        res = max(costTo)
        return res if res < float("inf") else -1