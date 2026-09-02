class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if not len(hand) % groupSize == 0:
            return False
        
        vals = {}
        for n in hand:
            vals[n] = vals.get(n,0) + 1
        
        for _ in range(len(hand) // groupSize):
            m = min(vals)
            for i in range(m, m + groupSize):
                if i not in vals:
                    return False
                vals[i] -= 1
                if vals[i] == 0:
                    del vals[i]
        
        return True