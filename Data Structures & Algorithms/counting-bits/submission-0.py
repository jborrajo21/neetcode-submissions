class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)

        for i in range(n+1):
            count = 0
            n = i
            while n:
                n &= n -1
                count += 1
            output[i] = count
        
        return output