class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if not len(hand) % groupSize == 0:
            return False
        
        vals = {}
        for n in hand:
            vals[n] = vals.get(n,0) + 1
        
        for n in sorted(vals):
            if vals[n] > 0:
                count = vals[n]
                for i in range(n, n + groupSize):
                    if vals.get(i, 0) < count:
                        return False
                    vals[i] -= count
        
        return True