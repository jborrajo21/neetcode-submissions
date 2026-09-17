class Solution:
    def isHappy(self, n):
        def square_sum(x):
            s = 0
            while x:
                s += (x % 10) ** 2
                x //= 10
            return s
        
        slow, fast = n, square_sum(n)
        while fast != 1 and slow != fast:
            slow = square_sum(slow)
            fast = square_sum(square_sum(fast))
        return fast == 1
        