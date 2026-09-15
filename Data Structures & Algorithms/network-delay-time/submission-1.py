class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(set)
        for u,v,cost in times:
            g[u].add((cost,v))
        
        heap = [(0, k)]
        heapq.heapify(heap)

        costTo = [float("inf")] * n
        costTo[k-1] = 0

        while heap:
            prevCost, node = heapq.heappop(heap)
            for cost, n in g[node]:
                if cost + prevCost < costTo[n-1]:
                    heapq.heappush(heap, (cost + prevCost, n))
                    costTo[n-1] = cost + prevCost
        
        res = max(costTo)
        return res if res < float("inf") else -1