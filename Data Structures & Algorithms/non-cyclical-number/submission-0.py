class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            seen.add(n)
            s = 0
            while n:
                s += (n % 10)**2
                n = int(n/10)
            n = s
            if n in seen:
                return False
        
        return True