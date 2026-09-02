class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx = 0
        total = 0
        s = 0
        for i in range(len(gas)):
            n = gas[i] - cost[i]
            total += n
            s += n
            if s < 0:
                s = 0
                idx = i + 1
        
        return idx if total >= 0 else -1
