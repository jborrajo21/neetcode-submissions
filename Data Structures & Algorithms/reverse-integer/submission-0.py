class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        while x != 0:
            d = int(math.fmod(x,10))
            x = int(x / 10)
            res += d
            res *= 10
        
        res//=10

        return res if -(2**31) <= res < (2**31) else 0