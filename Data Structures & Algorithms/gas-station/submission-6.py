class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = 0
        s = 0
        total = 0
        for i in range(len(gas)):
            n = gas[i] - cost[i]
            total += n
            s += n
            if s < 0:
                res = i+1
                s = 0
        
        return res if total >= 0 else -1
