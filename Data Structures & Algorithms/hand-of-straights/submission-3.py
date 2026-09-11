class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        freqs = {}
        for n in hand:
            freqs[n] = freqs.get(n,0) + 1
        
        for n in sorted(freqs):
            num = freqs[n]
            if num > 0:
                for i in range(n, n + groupSize):
                    if i in freqs and freqs[i] >= num:
                        freqs[i] -= num
                    else:
                        return False
        
        return True
