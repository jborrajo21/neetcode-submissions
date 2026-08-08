class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minimum = r

        while l <= r:
            k = (l + r) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile/k)
            if time > h:
                l = k + 1
            else:
                minimum = min(minimum, k)
                r = k - 1

        return minimum 
